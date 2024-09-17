JAZZMIN_SETTINGS = {
    # Window and brand settings
    "site_title": "Library Admin",
    "site_header": "AutoHoulEx",
    "site_brand": "AutoHoulEx",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to the library",
    "copyright": "Acme Library Ltd",
    "search_model": ["autohoulex.Orders", "autohoulex.Post"],
    "user_avatar": None,

    ############
    # Top Menu #
    ############
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "autohoulex.Orders"},
        {"model": "autohoulex.Post"},
    ],

    #############
    # User Menu #
    #############
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # Order of apps and models in the sidebar
    "order_with_respect_to": [
        "auth",
        "autohoulex.Orders",
        "autohoulex.Post",
        "autohoulex.Post",
        "autohoulex.Comment",
    ],

    # Custom icons for apps and models
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "autohoulex.Orders": "fas fa-box",
        "autohoulex.Post": "fas fa-newspaper",
        "autohoulex.Comment": "fas fa-comments",
        "autohoulex.Make": "fas fa-plus",
        "autohoulex.Model": "fas fa-car",
        "autohoulex.Year": "fas fa-calendar",
        "autohoulex.ContactMessage": "fas fa-contact",

    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}
