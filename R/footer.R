footer = load_html("views/footer.html")
footer = gsub("\\{(date)\\}", get_date(), footer)
cat(footer)
