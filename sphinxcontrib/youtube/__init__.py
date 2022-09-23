"""Sphinx "youtube" extension"""
from . import utils, vimeo, youtube

__version__ = "100.2.1"


def setup(app):
    app.add_node(youtube.youtube, **youtube._NODE_VISITORS)
    app.add_directive("youtube", youtube.YouTube)
    app.add_node(vimeo.vimeo, **vimeo._NODE_VISITORS)
    app.add_directive("vimeo", vimeo.Vimeo)
    app.connect("builder-inited", utils.configure_image_download)
    app.connect("env-merge-info", utils.merge_download_images)
    app.connect("env-updated", utils.download_images)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
