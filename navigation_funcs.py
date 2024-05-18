import streamlit as st

def nav_bar(left: tuple[str, str] = None,
               middle: tuple[str, str] = None,
               right: tuple[str, str] = None):

    """Creates a navigation bar with three buttons.
    
    Params:
        
        left (tuple): A tuple containing the button label and the page path.
        
        middle (tuple): A tuple containing the button label and the page path.
        
        right (tuple): A tuple containing the button label and the page path.
        
    
    Returns:
        None
    
    """

    col_1, col_2, col_3 = st.columns(3)
    
    with col_1:
        if st.button(left[0]):
            st.switch_page(left[1])
    with col_2:
        if st.button(middle[0]):
            st.switch_page(middle[1])
    with col_3:
        if st.button(right[0]):
            st.switch_page(right[1])