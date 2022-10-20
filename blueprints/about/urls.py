from views import about, about_me, about_my_work

about.add_url_rule('/aboutMe', 'about_me', about_me)
about.add_url_rule('/aboutMyWork', 'about_my_work', about_my_work)
