build_sidebar_section(category, root_pages) {
    let sidebar_section = $(
        `<div class="standard-sidebar-section nested-container" data-title="${category.id}"></div>`
    );

    let $title = $(`<button class="btn-reset standard-sidebar-label">
        <span>${frappe.utils.icon("es-line-down", "xs")}</span>
        <span class="section-title">${category.label}<span>
    </div>`).appendTo(sidebar_section);
    $title.attr({
        "aria-label": __("Toggle Section: {0}", [category.label]),
        "aria-expanded": "true",
    });
    this.prepare_sidebar(root_pages, sidebar_section, this.sidebar);

    $title.on("click", (e) => {
        const $e = $(e.target);
        const href = $e.find("span use").attr("href");
        const isCollapsed = href === "#es-line-down";
        let icon = isCollapsed ? "#es-line-right-chevron" : "#es-line-down";
        $e.find("span use").attr("href", icon);
        $e.parent().find(".sidebar-item-container").toggleClass("hidden");
        $e.attr("aria-expanded", String(!isCollapsed));
    });

    if (Object.keys(root_pages).length === 0) {
        sidebar_section.addClass("hidden");
    }

    $(".item-anchor").on("click", () => {
        $(".list-sidebar.hidden-xs.hidden-sm").removeClass("opened");
        $(".close-sidebar").css("display", "none");
        $("body").css("overflow", "auto");
    });

    if (
        sidebar_section.find(".sidebar-item-container").length &&
        sidebar_section.find("> [item-is-hidden='0']").length == 0
    ) {
        sidebar_section.addClass("hidden show-in-edit-mode");
    }
}