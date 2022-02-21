def define_env(env):
    "Hook function"

    @env.macro
    def test123(page):
        page_list = []
        this_page = page.next_page
        while this_page:
            page_list.append(this_page)
            this_page = this_page.next_page
        return page_list
    
