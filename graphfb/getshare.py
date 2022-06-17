# import facebook as fb
# access_token = "EAAGNO4a7r2wBAF9pNedHjo7z37dBgsLAUOr7Dxpy5U51xcVm5cfWakZAoZC2AjBC7uZB0jV77ygJGnLRDk4UBVqtkaZCUFwXDOZA5hWCADkVYRDPXZC2zRjitmHrLIcV1mONGJSnmDlF5R7wUGCKkE0sNrSZBtco5OKlz2hdhfABkie5hjQz4UR"
# asfb = fb.GraphAPI(access_token)
# shares = asfb.get_connections('107512638440091_764346994522777','sharedposts',limit = 1)
# idShare = shares['data'][0]['id'].split("_")[0]
# print(idShare)

# import streamlit as st
# from phonenumbers import geocoder, carrier, timezone
# import phonenumbers
# def main():
#     st.title("Định vị SĐT và nhà cung cấp dịch vụ")
#     mobile_number=st.text_input("Nhập số điện thoại: ",type="password")
#     if st.button("Track"):
#         ch_number=phonenumbers.parse(mobile_number,'CH')
#         st.success("Quốc gia: {}".format(geocoder.description_for_number(ch_number,"en")))
#         services_operator=phonenumbers.parse(mobile_number, 'RO')
#         st.success("Nhà cung cấp: {}".format(carrier.name_for_number(services_operator, "en")))
#         gb_number = phonenumbers.parse(mobile_number, "GB")
#         st.success("TimeZone: {}".format(timezone.time_zones_for_number(gb_number)))
# if __name__=="__main__":
#     main()



from requests import session
s = session()
access_token = """EAAGNO4a7r2wBALUH5wPY7IBUQ5TPmT5CtYDZB1HHPXBZASo5Cou8ginIA0RZAsv1DjBEm1geiHea5GyaenOxENuMkKCjDor8DzZBg2zlfZB1ZCrsgZCZATPjZCgtm58LDzKsoAZA2spxJJ1xvlaZAUULcfZBpxhJfzlz8NEnWcYXZCz35p8C2apS4HbKi"""
url = 'https://graph.facebook.com/v2.0/971464953226147?fields=comments.limit(0).summary(true),likes.limit(0).summary(true)&access_token='+access_token
url = 'https://graph.facebook.com/v2.0/971464953226147?fields=comments.limit(50).summary(true)&access_token='+access_token
p = s.get(url)
print(p.json())