import streamlit as st

st.write("Deploy Success")

# st.markdown(
#     """
#     <style>
#         div[data-testid="stSidebar"] {
#             width: 250px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# class MultiApp:
#     def __init__(self):
#         self.apps = []

#     def add_app(self, title, func):
#         self.apps.append({
#             "title": title,
#             "function": func
#         })

#     def run():
#         with st.sidebar:        
#             app = option_menu(
#                 menu_title="Real-Time Analytics",
#                 options=['Tiếp nhận dữ liệu', 'Báo cáo tổng hợp'],
#                 icons=['cloud-upload','person-circle'],
#                 menu_icon='house-fill',
#                 default_index=0,
#                 styles={
#                     "container": {"padding": "5!important","background-color":'black'},
#                     "icon": {"color": "white", "font-size": "20px"}, 
#                     "nav-link": {"color":"white","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
#                     "nav-link-selected": {"background-color": "#02ab21"},
#                     "menu-title": {"color": "white"}}
#             )
#         if app == "Tiếp nhận dữ liệu":
#             data.app()    
#         if app == "Báo cáo tổng hợp":
#             userinterface.app()  

# if __name__ == "__main__":          
#     MultiApp.run()
