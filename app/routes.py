from flask import Blueprint, abort, render_template, request

from .services.content_service import ContentError, ContentLibrary

main_bp = Blueprint("main", __name__)
library = ContentLibrary()


@main_bp.context_processor
def inject_navigation():
    tree = library.get_tree()
    return {
        "sidebar_tree": tree,
        "first_leaf": library.get_first_leaf(tree),
    }


@main_bp.route("/")
def index():
    tree = library.get_tree()
    featured_item = library.get_first_leaf(tree)
    return render_template("index.html", tree=tree, featured_item=featured_item)


@main_bp.route("/items/<path:item_path>/")
def item_view(item_path: str):
    try:
        node = library.get_node(item_path.split("/"))
    except ContentError as exc:
        abort(404, description=str(exc))

    if not node["is_leaf"]:
        abort(404, description="This item is an organizational container only.")

    requested_tab = request.args.get("tab")
    active_tab, rendered_content = library.get_node_tab_content(node, requested_tab)

    return render_template(
        "topic.html",
        topic=node,
        active_tab=active_tab,
        rendered_content=rendered_content,
    )
