footer = load_html("../docs/footer.html")
footer = gsub("\\{(date)\\}", get_date(), footer)
cat(footer)
