datatable(
    get_data(),
    rownames = FALSE,
    class = 'cell-border stripe hover',
    style = 'bootstrap',
    escape = FALSE,
    extensions = c('ColReorder', 'FixedHeader', 'Responsive'),
    options = list(
        language = list(url = 'https://raw.githubusercontent.com/subreddit-emportugues/lista/master/lang.json'),
        pageLength = 25,
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
                width = '150px',
                targets = c(0)
            )
        )
    )
)
