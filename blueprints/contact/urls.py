from views import contact, contact_me, contact_for_sponsor


contact.add_url_rule('/contactMe', 'contact_me', contact_me)
contact.add_url_rule('/contactForSponsor', 'contact_for_sponsor', contact_for_sponsor)