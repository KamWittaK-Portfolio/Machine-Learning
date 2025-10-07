import uuid, os
from typing import Optional
from dotenv import load_dotenv
from zenml.client import Client
from zenml.models.v2.core.component import ComponentUpdate, ComponentFilter

load_dotenv()

def update_artifact_store_client_kwargs(store_name: Optional[str] = None):
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
    client_kwargs.update({"endpoint_url": os.getenv("ARTIFACT_URL")})


    current_config["client_kwargs"] = {"endpoint_url": os.getenv("ARTIFACT_URL")}
    current_config["key"] = os.getenv("ARTIFACT_KEY")
    current_config["secret"] = os.getenv("ARTIFACT_SECRET")
    current_config["path"] = os.getenv("ARTIFACT_PATH")

    # Create a ComponentUpdate with the full preserved configuration
    component_update = ComponentUpdate(configuration=current_config)

    try:
        updated = client.zen_store.update_stack_component(component_id, component_update)
        print(f"Artifact store updated")
    except Exception as exc:
        raise RuntimeError(f"Failed to update artifact store: {exc}") from exc
    

def update_tracking_server_credentials(server_name: Optional[str] = None):
    client = Client()

    # List components and find the tracking server by name
    filter_model = ComponentFilter()
    page = client.zen_store.list_stack_components(filter_model, hydrate=True)
    found = None
    for comp in page.items:
        if getattr(comp, "name", None) == server_name:
            found = comp
            break

    if found is None:
        raise ValueError(f"No stack component named '{server_name}' found")

    hydrated = found
    component_id = getattr(found, "id", None) or getattr(found, "uuid", None)
    if isinstance(component_id, str):
        component_id = uuid.UUID(component_id)

    if component_id is None:
        raise RuntimeError("Resolved component id is None")

    # Convert configuration model to plain dict
    raw_config = getattr(hydrated, "configuration", {}) or {}
    if hasattr(raw_config, "model_dump"):
        current_config = raw_config.model_dump()  # type: ignore
    elif hasattr(raw_config, "dict"):
        current_config = raw_config.dict()  # type: ignore
    else:
        current_config = dict(raw_config)

    # Update tracking server credentials
    current_config["tracking_uri"] = os.getenv("TRACKER_URL")
    current_config["tracking_username"] = os.getenv("TRACKER_USER")
    current_config["tracking_password"] = os.getenv("TRACKER_PASSWORD")
    current_config["tracking_token"] = os.getenv("TRACKER_TOKEN")

    # Create a ComponentUpdate with the updated configuration
    component_update = ComponentUpdate(configuration=current_config)

    try:
        updated = client.zen_store.update_stack_component(component_id, component_update)
        print(f"Tracking server '{server_name}' updated successfully")
    except Exception as exc:
        raise RuntimeError(f"Failed to update tracking server: {exc}") from exc
