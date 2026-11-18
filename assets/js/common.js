$(document).ready(function () {
  // add toggle functionality to abstract and bibtex buttons
  $("a.abstract").click(function () {
    $(this).parent().parent().find(".abstract.hidden").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.bibtex").click(function () {
    $(this).parent().parent().find(".bibtex.hidden").toggleClass("open");
    $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open");
  });
  $("a").removeClass("waves-effect waves-light");

  // Provide publication discovery links in addition to DOI and BibTeX.
  $(".publication-catalog ol.bibliography > li").each(function () {
    const title = $(this).find(".title").first().text().trim();
    const links = $(this).find(".links").first();
    if (!title || !links.length || links.find(".publication-search-link").length) return;
    const encodedTitle = encodeURIComponent(title);
    $("<a>", {
      class: "btn btn-sm z-depth-0 publication-search-link",
      href: `https://pubmed.ncbi.nlm.nih.gov/?term=${encodedTitle}`,
      target: "_blank",
      rel: "noopener noreferrer",
      text: "PubMed",
    }).insertBefore(links.find(".bibtex-details").first());
    $("<a>", {
      class: "btn btn-sm z-depth-0 publication-search-link",
      href: `https://scholar.google.com/scholar?q=${encodedTitle}`,
      target: "_blank",
      rel: "noopener noreferrer",
      text: "Scholar",
    }).insertBefore(links.find(".bibtex-details").first());
  });

  // bootstrap-toc
  if ($("#toc-sidebar").length) {
    // remove related publications years from the TOC
    $(".publications h2").each(function () {
      $(this).attr("data-toc-skip", "");
    });
    var navSelector = "#toc-sidebar";
    var $myNav = $(navSelector);
    Toc.init($myNav);
    $("body").scrollspy({
      target: navSelector,
    });
  }

  // add css to jupyter notebooks
  const cssLink = document.createElement("link");
  cssLink.href = "../css/jupyter.css";
  cssLink.rel = "stylesheet";
  cssLink.type = "text/css";

  let theme = localStorage.getItem("theme");
  if (theme == null || theme == "null") {
    const userPref = window.matchMedia;
    if (userPref && userPref("(prefers-color-scheme: dark)").matches) {
      theme = "dark";
    }
  }

  $(".jupyter-notebook-iframe-container iframe").each(function () {
    $(this).contents().find("head").append(cssLink);

    if (theme == "dark") {
      $(this).bind("load", function () {
        $(this).contents().find("body").attr({
          "data-jp-theme-light": "false",
          "data-jp-theme-name": "JupyterLab Dark",
        });
      });
    }
  });
});
