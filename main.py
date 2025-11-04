import streamlit as st
from src import config, session
from src.pages import all_rules_page, single_rule_page


def main():
    # app config
    st.set_page_config(
        page_title=config.APP_TITLE,
        page_icon=config.APP_ICON,
        menu_items={},
    )

    # user id
    session.init_user_id()

    pg = st.navigation(
        {
            "🔥 Eksperimen": [
                st.Page(
                    single_rule_page,
                    title="Uji Coba 1 Rule",
                    icon=":material/horizontal_rule:",
                ),
                st.Page(
                    all_rules_page,
                    title="Uji Coba Semua Rule",
                    icon=":material/density_small:",
                ),
            ]
        },
        expanded=True,
    )

    pg.run()


if __name__ == "__main__":
    main()
