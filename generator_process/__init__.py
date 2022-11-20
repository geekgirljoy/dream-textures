from .actor import Actor

class Generator(Actor):
    """
    The actor used for all background processes.
    """

    from .actions.prompt_to_image import prompt_to_image
    from .actions.upscale import upscale
    from .actions.huggingface_hub import hf_snapshot_download, hf_list_models, hf_list_installed_models