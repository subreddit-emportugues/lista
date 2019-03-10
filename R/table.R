datatable(
    get_data(),
    rownames = FALSE,
    class = 'cell-border stripe hover',
    style = 'bootstrap',
    escape = FALSE,
    extensions = c('ColReorder', 'FixedHeader', 'Responsive'),
    options = list(
        language = list(
            url = 'https://raw.githubusercontent.com/subreddit-emportugues/lista/master/res/lang/pt_BR.json',
            searchPlaceholder = 'Pesquisar'
        ),
        pageLength = 100,
        searchHighlight = TRUE,
        autoWidth = TRUE,
        searchDelay = 300,
        lengthMenu = c(5, 25, 100, 500, 1000),
        colReorder = TRUE,
        fixedHeader = TRUE,
        order = list(
            list(2, 'desc')
        ),
        columnDefs = list(
            list(
                width = '160px',
                targets = c(0)
            ),
            list(
                width = '350px',
                targets = c(1)
            ),
            list(
                render = JS(
                    "function(data, type) {",
                        "if (type != 'display') {",
                            "return parseInt(data.replace('.', ''))",
                        "}",
                        "return data",
                    "}"
                ),
                targets =  c(2)
            ),
            list(
                render = JS(
                    "function(data, type) {",
                        "if (type != 'display') {",
                            "return new Date(data.split('/').reverse().join('-')).getTime() / 1000",
                        "}",
                        "return data",
                    "}"
                ),
                targets = c(3)
            )
        )
    )
)
