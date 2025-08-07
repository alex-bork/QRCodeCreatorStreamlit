from abc import ABC, abstractmethod
import io
from typing import Dict, Literal, Optional, Tuple
import streamlit as st
import qrcode_creator as qc


class QRTypeBase(ABC):

    @abstractmethod
    def show_parameter(self) -> None:
        ...

    @abstractmethod
    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ):
        ...


class QRFactory:

    __types = [
        "Text",
        "Link",
        "Email",
        "Phone",
        "SMS",
        "Geolocation",
        "WiFi",
        "VCard"
    ]

    @classmethod
    def get_qr_types(cls) -> Dict:
        return cls.__types

    @classmethod
    def get_type_object(cls, qr_type: str) -> QRTypeBase:

        if qr_type not in cls.__types:
            raise ValueError(f"QR type '{qr_type}' not supported.")

        if qr_type == "Text":
            return QRTypeText()
        if qr_type == "Link":
            return QRTypeLink()
        if qr_type == "Geolocation":
            return QRTypeGeo()
        if qr_type == "Phone":
            return QRTypePhone()
        if qr_type == "SMS":
            return QRTypeSMS()
        if qr_type == "Email":
            return QRTypeEmail()        
        if qr_type == "WiFi":
            return QRTypeWifi()        
        if qr_type == "VCard":
            return QRTypeVCard()


class QRTypeText(QRTypeBase):

    def show_parameter(self): 
        self.__text = st.text_area("Text")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:

        if len(self.__text) == 0:
            raise ValueError("Text area is empty.")
        img = qc.QRCodeText(self.__text).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes


class QRTypeLink(QRTypeBase):

    def show_parameter(self):
        self.__link = st.text_input("Link")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:

        img = qc.QRCodeLink(self.__link).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes


class QRTypePhone(QRTypeBase):

    def show_parameter(self):
        self.__phone = st.text_input("Phone number")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:

        img = qc.QRCodePhone(self.__phone).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes


class QRTypeSMS(QRTypeBase):

    def show_parameter(self):
        self.__phone = st.text_input("Phone number")
        self.__sms = st.text_area("SMS text")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:

        img = qc.QRCodeSMS(self.__phone, self.__sms).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes


class QRTypeEmail(QRTypeBase):

    def show_parameter(self):
        self.__email = st.text_input("Email")
        self.__subject = st.text_input("Subject")
        self.__text = st.text_area("Text")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:

        img = qc.QRCodeEmail(self.__email, self.__subject, self.__text).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes


class QRTypeGeo(QRTypeBase):

    def show_parameter(self):
        col1, col2 = st.columns(2)
        self.__lat = col1.text_input("Latitude")
        self.__lon = col2.text_input("Longitude")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:

        loc = qc.QRCodeGeoLocationData(self.__lat, self.__lon)
        img = qc.QRCodeGeoLocation(loc).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes


class QRTypeWifi(QRTypeBase):

    def show_parameter(self):
        self.__ssid = st.text_input("SSID")
        self.__hidden = st.checkbox("Hiden")
        self.__encrypt = st.selectbox("Encryption", ["WPA", "WEP"])
        self.__pw = st.text_input("Password", type="password")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:
        img = qc.QRCodeWifi(
            self.__ssid,
            qc.WifiEncryption[self.__encrypt],
            self.__pw,
            self.__hidden,
        ).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes


class QRTypeVCard(QRTypeBase):

    def show_parameter(self):
        col1, col2 = st.columns(2)
        self.__fname = col1.text_input("First name")
        self.__lname = col2.text_input("Last name")
        col1, col2 = st.columns(2)
        self.__job = col1.text_input("Job title")
        self.__org = col2.text_input("Organisation")
        col1, col2 = st.columns(2)
        self.__phone = col1.text_input("Phone number")
        self.__email = col2.text_input("Email")
        self.__homepage = st.text_input("Homepage")

    def create_qr(
        self,
        qr_color_rgb: Tuple[int, int, int],
        bg_color_rgb: Tuple[int, int, int],
        format: Literal["PNG", "JPEG"] = "PNG",
        module_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
        eye_style=Optional[
            Literal[
                "squared",
                "gapped",
                "circle",
                "rounded",
                "verticalbars",
                "horizontalbars",
            ]
        ],
    ) -> qc.QRCodeText:
        img = qc.QRCodeVCard(
            self.__fname,
            self.__lname,
            organisation=self.__org,
            jobtitle=self.__job,
            phones=[qc.QRCodeVCardPhone(self.__phone)],
            emails=[qc.QRCodeVCardEmail(self.__email)],
            urls=[qc.QRCodeVCardUrl(self.__homepage)],
        ).create_image(
            fill_color=qr_color_rgb,
            back_color=bg_color_rgb,
            module_style=module_style,
            eye_style=eye_style,
        )
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=format)
        return img_bytes
