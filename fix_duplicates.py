with open('index.html', 'r') as f:
    content = f.read()

# The CSS block starts with /* --- GLOBAL ANIMATION PREFERENCES --- */
marker = '/* --- GLOBAL ANIMATION PREFERENCES --- */'
parts = content.split(marker)

if len(parts) > 2:
    # It was injected twice!
    # The first injection is parts[1]. The second is parts[2].
    # parts[2] contains the CSS block up to </style>, and then whatever follows it.
    
    # We want to keep parts[0], marker, parts[1], but for parts[2], we want to remove the CSS block.
    # Actually, parts[2] looks like: `...css block...</style>  ...rest of html...`
    # Let's just find the closing </style> in parts[2] and keep everything after it.
    css_end = parts[2].find('</style>')
    if css_end != -1:
        rest_of_html = parts[2][css_end:]
        new_content = parts[0] + marker + parts[1] + rest_of_html
        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Duplicate CSS removed!")
    else:
        print("Could not find </style> in the second injected block.")
else:
    print("No duplicates found.")
