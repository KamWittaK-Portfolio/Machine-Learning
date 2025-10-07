import uuid
from typing import Optional
from dotenv import load_dotenv
from zenml.client import Client
from zenml.models.v2.core.component import ComponentUpdate, ComponentFilter

load_dotenv()

def update_artifact_store_client_kwargs(new_client_kwargs: dict, *, store_name: Optional[str] = None, store_id: Optional[str] = None):
    client = Client()


    # list components and find by name
    filter_model = ComponentFilter()
    page = client.zen_store.list_stack_components(filter_model, hydrate=True)
    found = None
    for comp in page.items:
        if getattr(comp, "name", None) == store_name:
            found = comp
            break
    if found is None:
        raise ValueError(f"No stack component named '{store_name}' found")
    hydrated = found
    component_id = getattr(found, "id", None) or getattr(found, "uuid", None)
    if isinstance(component_id, str):
        component_id = uuid.UUID(component_id)
    

    if component_id is None:
        raise RuntimeError("Resolved component id is None")

    # Convert configuration model to plain dict
    raw_config = getattr(hydrated, "configuration", {}) or {}
    if hasattr(raw_config, "model_dump"):
        current_config = raw_config.model_dump() # type: ignore
    elif hasattr(raw_config, "dict"):
        current_config = raw_config.dict()  # type: ignore
    else:
        current_config = dict(raw_config)

    # Merge client kwargs
    client_kwargs = current_config.get("client_kwargs") or {}
    client_kwargs.update(new_client_kwargs)
    current_config["client_kwargs"] = client_kwargs

    # Create a ComponentUpdate with the full preserved configuration
    component_update = ComponentUpdate(configuration=current_config)

    try:
        updated = client.zen_store.update_stack_component(component_id, component_update)
        print(f"Artifact store updated")
    except Exception as exc:
        raise RuntimeError(f"Failed to update artifact store: {exc}") from exc