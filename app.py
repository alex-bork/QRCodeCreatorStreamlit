import streamlit as st
from modules import *
from uuid import uuid4


def show_downloaded_message():
    st.toast("QR has been downloaded.", icon=":material/check:")


def check_filename(filename):
    if filename[-4::] != ".png":
        return f"{filename}.png"
    else:
        return filename


def on_filename_changed(par):
    pass


def hex_to_rgb(hex):
    hex = hex[1::]
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


def on_type_changed():
    if "create_clicked" in st.session_state:
        del st.session_state.create_clicked

filetypes = ["PNG", "JPEG"]

style_mapping = {
    "Square": "square",
    "Gapped Square": "gapped",
    "Circle": "circle",
    "Rounded": "rounded",
    "Vertical Bars": "verticalbars",
    "Horizontal Bars": "horizontalbars",
}

if not "qr_color" in st.session_state:
    st.session_state.qr_color = "#000000"
    st.session_state.bg_color = "#ffffff"
    # st.session_state.filetype = filetypes[0]


with st.sidebar:
    st.title("Settings")
    st.subheader("File type")
    st.selectbox(
        "File type field",
        filetypes,
        label_visibility="collapsed",
        key="filetype",
    )
    st.subheader("Colors")
    col0, col1, col2 = st.columns([1,3,1])
    col0.color_picker("QR", key="qr_color")
    col1.color_picker("Background", key="bg_color")
    st.subheader("QR style")
    st.selectbox("QR module style", ["Square", "Gapped Square", "Circle", "Rounded", "Vertical Bars", "Horizontal Bars"], key="qr_mod_style")
    st.selectbox(
        "QR eye style",
        [
            "Square",
            "Gapped Square",
            "Circle",
            "Rounded",
            "Vertical Bars",
            "Horizontal Bars",
        ], key="qr_eye_style"
    )

qr_types = QRFactory.get_qr_types()

type_selected = st.selectbox("QR type", qr_types, on_change=on_type_changed)

try:

    if type_selected:

        qr_object = QRFactory.get_type_object(type_selected)

        if qr_object:

            qr_object.show_parameter()

            col1, col2, col3 = st.columns([1,1,1])
            create_clicked = col2.button(
                        "Create QR", 
                        type="primary", 
                        icon=":material/add_photo_alternate:",
                        use_container_width=True
                    )

            if create_clicked:
                st.session_state.create_clicked = True
                uuid = str(uuid4())
                st.session_state.download_filename = f"QR-{uuid[0:3]}{uuid[-3::]}"

            if "create_clicked" in st.session_state:
                qr = qr_object.create_qr(
                    hex_to_rgb(st.session_state.qr_color),
                    hex_to_rgb(st.session_state.bg_color),
                    st.session_state.filetype,
                    style_mapping[st.session_state.qr_mod_style],
                    style_mapping[st.session_state.qr_eye_style],
                )
                col1, col2, col3 = st.columns(3)
                col2.image(qr)

                col1, col2, col3 = st.columns([1, 1, 1])

                filename = col2.text_input(
                    "File name",
                    value=st.session_state.download_filename,
                )

                col1, col2, col3 = st.columns([1,1,1])
                col2.download_button(
                    "Download QR",
                    qr,
                    (
                        filename
                        if filename[-4::] == f".{st.session_state.filetype.lower()}"
                        else f"{filename}.{st.session_state.filetype.lower()}"
                    ),
                    type="primary",
                    icon=":material/download:",
                    use_container_width=True,
                    on_click=show_downloaded_message,
                )

        else:
            st.error("QR object empty.")

except Exception as ex:
    st.error(ex)
