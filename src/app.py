import webbrowser
import flet as ft
from flet import BottomSheet, ButtonStyle, Column, Container, Image, Markdown, Page, Row, Text, TextButton, Divider

c_blue = "#013d82"
c_lightblue = "#026be3"

f_normal = 16
f_heading = 32
f_subheading = 24

btn_style = ButtonStyle(
    color = {
        "hovered": ft.colors.BLACK,
        "focused": ft.colors.WHITE,
        "": ft.colors.WHITE,
    },
    bgcolor = {
        "hovered": ft.colors.WHITE,
        "focused": c_blue,
        "": c_blue,
    },
)

intro_str = """Welcome to the SASSDA Atmospheric Corrosion Application! This application can be used to determine the most suitable materials for a user-specified environment that may be susceptible to atmoshperic corrosion."""
about_str = """Atmospheric corrosion is the corrosion of metals exposed to air and its pollutants. It is an electrochemical process where a film of electrolyte forms on the metal surface due to condensation or even dew. When air pollutants such as SO\u2082, CO\u2082, NO\u2093 and salts dissolve in a film of water, they increase its conductivity and corrosivity. Atmospheric corrosion is a serious worldwide problem affecting people in all walks of life. It is of concern to homeowners, architects, engineers, designers, maintenance personnel and accountants. All outdoor and indoor materials exposed to the elements are potentially subjected to degradation resulting from atmospheric conditions. SO\u2082, CO\u2082, NO\u2093 and salts dissolve in a film of water, they increase its conductivity and corrosivity. Atmospheric corrosion is a serious worldwide problem affecting people in all walks of life. It is of concern to homeowners, architects, engineers, designers, maintenance personnel and accountants. All outdoor and indoor materials exposed to the elements are potentially subjected to degradation resulting from atmospheric conditions."""
factors_str = "\u2022 Polluted environments that can be regarded as rural.\n\u2022 Exposure to salt, defined as the distance from marine area, and de-icing salt exposure (normally in Europe and US).\n\u2022 Weather including temperatures, humidity and rainfall.\n\u2022 Design includes surfaces facilitating rain cleaning or the presence of crevices, as well as surface condition of stainless steel.\n\u2022 Maintenance stipulating the cleaning frequency."

lst1 = [
    ("Controlled (Internally controlled environment)", 1),
    ("Low (M > 10km  OR  S > 0.1km)", 0),
    ("Medium (5km < M <= 10km  OR  0.01km < S <= 0.1km)", -3),
    ("High (0.5km < M <= 5km  OR  S <= 0.01km)", -7),
    ("Very High (M <= 0.5km)", -10),
    ("Severe (M <= 0.25km)", -15)
]
lst2 = [
    ("Low (10 μg/m³ average deposition)", 0),
    ("Medium (10 to 90 μg /m³ average deposition)", -5),
    ("High (90 to 250 μg /m³ average deposition)", -10)
]
lst3 = [
    ("Low (Fully exposed to washing by rain)", 0),
    ("Medium (Specified cleaning regime)", -2),
    ("High (No washing by rain /No specified cleaning)", -7)
]

options1, options2, options3 = [], [], []
for o1 in lst1:
    options1.append(ft.dropdown.Option(o1[0]))
for o2 in lst2:
    options2.append(ft.dropdown.Option(o2[0]))
for o3 in lst3:
    options3.append(ft.dropdown.Option(o3[0]))

dropdown1 = Container(
    content=ft.Dropdown(
        options=options1,
        width=800,
        text_size=f_normal,
        border_color=ft.colors.WHITE,
        focused_border_color=ft.colors.WHITE,
        border_radius=20,
        hint_text="F1"
    ),
    bgcolor=ft.colors.WHITE,
    border_radius=ft.border_radius.all(20)
)

dropdown2 = Container(
    content=ft.Dropdown(
        options=options2,
        width=800,
        text_size=f_normal,
        border_color=ft.colors.WHITE,
        focused_border_color=ft.colors.WHITE,
        border_radius=20,
        hint_text="F2"
    ),
    bgcolor=ft.colors.WHITE,
    border_radius=ft.border_radius.all(20)
)

dropdown3 = Container(
    content=ft.Dropdown(
        options=options3,
        width=800,
        text_size=f_normal,
        border_color=ft.colors.WHITE,
        focused_border_color=ft.colors.WHITE,
        border_radius=20,
        hint_text="F3"
    ),
    bgcolor=ft.colors.WHITE,
    border_radius=ft.border_radius.all(20)
)

class1 = ["3CR12 (Ferritic)", "430 (Ferritic)", "409 (Ferritic)"]
class2 = ["304 (MO Austenitic)", "304L (MO Austenitic)", "304LN (MO Austenitic)", "321 (MO Austenitic)", "301LN (MO Austenitic)", "304 DDQ (MO Austenitic)", "304Cu (MO Austenitic)", "2001 (Lean Duplex)"]
class3 = ["316 (Standard Austenitic)", "316L (Standard Austenitic)", "316L2.5Mo (Standard Austenitic)", "316Ti (Standard Austenitic)", "316LN (Standard Austenitic)", "316LCu (Standard Austenitic)", "2404 (Standard Austenitic)", "2304 (Lean Duplex)", "2202 (Lean Duplex)", "2102 (Lean Duplex)"]
class4 = ["317LMN (Super Austenitic)", "904L (Super Austenitic)", "2205 (Duplex / Super Duplex)"]
class5 = ["254SMO (Super Austenitic)", "S34565 (Super Austenitic)", "NO8926 (Super Austenitic)", "2507 (Duplex / Super Duplex)", "S32760 (Duplex / Super Duplex)", "UNS32520 (Duplex / Super Duplex)"]

def initPage(page : Page):
    page.scroll = "auto"
    page.bgcolor = ft.colors.WHITE
    page.title = "SASSDA: Atmospheric Corrosion Application"

    def open_dialog():
        dialog.open = True
        dialog.update()

    def close_dialog():
        dialog.open = False
        dialog.update()

    dialog = BottomSheet(
        Container(
            Column(
                [
                    Text(
                        value=intro_str,
                        text_align="center",
                        size=f_normal,
                    ),
                    TextButton(
                        content=Text("Close", size=f_normal),
                        style=btn_style,
                        width=200,
                        on_click=lambda _: close_dialog()
                    ),
                ],
                horizontal_alignment="center",
                tight=True,
            ),
            padding=10,
        ),
        open=True,
        on_dismiss=lambda _: close_dialog()
    )

    title = Container(
        content=Text(
            value="Atmospheric Corrosion Application",
            color=c_blue,
            size=48,
            bgcolor=ft.colors.WHITE,
            weight="bold",
            text_align="center"
        ),
        alignment=ft.alignment.center,
    )

    banner = Container(
        content=Image(
            src = f"banner.png",
            fit = "fitWidth",
            border_radius = ft.border_radius.all(30)
        ),
        alignment=ft.alignment.center
    )

    contents = Container(
        bgcolor=c_lightblue,
        padding=10,
        alignment=ft.alignment.center,
        border_radius=20
    )

    navbar = Container(
        content=Row(
            controls=[
                TextButton(
                    content=Text("About", size=f_normal),
                    style=btn_style,
                    width=240,
                    on_click=lambda _: showAbout(
                        page,
                        contents
                    ),
                ),
                TextButton(
                    content=Text("Corrosion Factors", size=f_normal),
                    style=btn_style,
                    width=240,
                    on_click=lambda _: showCFs(
                        page,
                        contents
                    )
                ),
                TextButton(
                    content=Text("Environment Selector", size=f_normal),
                    style=btn_style,
                    width=240,
                    on_click=lambda _: showSelector(
                        page,
                        contents
                    )
                )
            ],
            spacing=20, #double default
            alignment="center",
        ),
        bgcolor=c_lightblue,
        padding=15,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(10)
    )

    banner = Container(
        content=Image(
            src = f"banner.png",
            fit = "fitWidth",
            border_radius = ft.border_radius.all(30)
        ),
        alignment=ft.alignment.center
    )

    page.add(
        Column(
            controls=[
                dialog,
                title,
                banner,
                navbar,
                contents,
            ],
            alignment="center",
        )
    )
    page.update()

    showAbout(page, contents)
    open_dialog()


def showAbout(page : Page, contents : Container):
    contents.content = Column(
        controls=[
            Text(
                value="",
                size=2,
            ),
            Container(
                content=Text(
                    value=" Information about atmoshperic corrosion ",
                    size=f_heading,
                    text_align="center",
                    color=ft.colors.WHITE
                ),
                padding=15,
                border_radius = ft.border_radius.all(20),
                bgcolor=c_blue,
            ),
            Text(
                value="",
                size=7,
            ),
            Text(
                value=about_str,
                text_align="center",
                size=f_normal,
                color=ft.colors.WHITE
            ),
            Text(
                value="",
                size=7,
            ),
            Container(
                content=Image(
                    src = f"corrosion.png",
                    width = 400,
                    border_radius = ft.border_radius.all(15),
                ),
                alignment=ft.alignment.center
            ),
            Text(
                value="",
                size=20,
            ),
            Container(
                content=Column(
                    controls=[
                        Text(
                            value="This website is maintained by Lucas Meyer and Michel Basson.",
                            size=f_normal,
                            color=ft.colors.WHITE
                        ),
                        Row(
                            controls=[
                                Text(
                                    value="Contact: ",
                                    size=f_normal,
                                    color=ft.colors.WHITE
                                ),
                                Container(
                                    content=Image(
                                        src=f"mail.jpg",
                                        width=39,
                                        border_radius=7
                                    ),
                                    on_click=lambda _: showEmail(page)
                                ),
                                Container(
                                    content=Image(
                                        src=f"linkedin.png",
                                        width=40,
                                        border_radius=7
                                    ),
                                    on_click=lambda _: webbrowser.open("https://www.linkedin.com/in/lucas-meyer-33a820203/")
                                ),
                                Container(
                                    content=Image(
                                        src=f"git.png",
                                        width=38.3,
                                        border_radius=7
                                    ),
                                    on_click=lambda _: webbrowser.open("https://github.com/lucas-meyer-7")
                                )
                            ],
                            alignment="center"
                        )
                    ],
                    horizontal_alignment="center"
                ),
                bgcolor=c_lightblue,
                padding=10,
                alignment=ft.alignment.center,
                border_radius=20
            ),
            Text(
                value="",
                size=2,
            ),
        ],
        horizontal_alignment="center"
    )
    page.add()
    page.update()

def showCFs(page : Page, contents : Container):
    contents.content = Column(
        controls=[
            Text(
                value="",
                size=2,
            ),
            Container(
                content=Text(
                    value=" Causes of atmosphoric corrosion ",
                    size=f_heading,
                    text_align="center",
                    color=ft.colors.WHITE
                ),
                padding=15,
                border_radius = ft.border_radius.all(20),
                bgcolor=c_blue,
            ),    
            Text(
                value="",
                size=7,
            ),
            Text(
                value="Corrosion factors to take into account in determining the degree of corrosion to be expected",
                size=f_subheading,
                weight="bold",
                text_align="center",
                color=ft.colors.WHITE
            ),
            Text(
                value=factors_str,
                color=ft.colors.WHITE,
                size=f_normal
            ),
            Text(
                value="",
                size=2,
            ),
            Text(
                value="Grade selection and Estimated Life Span (ELS) of stainless steel fasteners in different atmospheric conditions",
                size=f_subheading,
                weight="bold",
                text_align="center",
                color=ft.colors.WHITE
            ),
            Container(
                content=Image(
                    src = f"selection_table.jpg",
                    border_radius = ft.border_radius.all(2),
                    width=1000,
                ),
                alignment=ft.alignment.center,
            ),
            Text(
                value="[*] Classification of ambient conditions according to EN ISO 12994-2.",
                width=600,
                size=f_normal,
                text_align="center",
                color=ft.colors.WHITE
            ),
            Text(
                value="[**] Estimated Life Span (ELS) is subject to: (1) correct material handling/fabrication, by avoiding carbon and iron contamination; (2) choosing the correct grade for the specified C class; (3) proper care and maintenance procedures/frequency, as per roofing sheeting or architectural application guidelines.",
                width=600,
                size=f_normal,
                text_align="center",
                color=ft.colors.WHITE
            ),
            Text(
                value="",
                size=10,
            ),
            Text(
                value="Corrosion Map of South Africa",
                size=f_subheading,
                weight="bold",
                text_align="center",
                color=ft.colors.WHITE
            ),
            Container(
                content=Image(
                    src = f"map.jpg",
                    width=900,
                    border_radius = ft.border_radius.all(15),
                ),
                alignment=ft.alignment.center
            ),
            Text(
                value="",
                size=10,
            ),
            Text(
                value="Life span comparison",
                size=f_subheading,
                weight="bold",
                text_align="center",
                color=ft.colors.WHITE
            ),
            Container(
                content=Image(
                    src = f"graph_table.jpg",
                    border_radius = ft.border_radius.all(15),
                ),
                alignment=ft.alignment.center
            ),
            Text(
                value="The graph shows the relative life span of various materials compared under the same functional conditions. Mild steel is the base for the comparison. As example this would indicate that in conditions where mild steel would last one year, grade 3CR12 would last an estimated 164 years. This also shows the iportance of Total Life Cycle Cost analysis before  final grade selection.",
                size=f_normal,
                text_align="center",
                color=ft.colors.WHITE
            ),
            Text(
                value="The table shows the result of corrosion tests done on various materials under various corrosion conditions. The bottom row shows the average over the range of conditions. As example, under severe marine conditions, grade 316 will suffer a material loss of 0,032mm per year whilst 3CR12 will lose and estimated 1,518mm over the same period.",
                size=f_normal,
                text_align="center",
                color=ft.colors.WHITE
            ),
            Text(
                value="",
                size=2,
            ),
        ],
        horizontal_alignment="center",
    )
    page.update()

def showSelector(page : Page, contents : Container):
    contents.content = Column(
        controls=[
            Text(
                value="",
                size=2,
            ),
            Container(
                content=Text(
                    value=" Material selection to EN 1993-1-4 for Southern African Conditions ",
                    size=f_heading,
                    text_align="center",
                    color=ft.colors.WHITE
                ),
                padding=15,
                border_radius = ft.border_radius.all(20),
                bgcolor=c_blue,
            ),
            Text(
                value="",
                size=7,
            ),
            Text(
                value="Select the environment below",
                size=f_subheading,
                text_align="center",
                weight="bold",
                color=ft.colors.WHITE
            ),
            Row(
                controls=[
                    Text(
                        "Risk of exposure to chlorides:",
                        size=f_normal,
                        width=280,
                        color=ft.colors.WHITE
                    ),
                    dropdown1
                ],
                alignment="center"
            ),
            Row(
                controls=[
                    Text(
                        "Risk of exposure to sulpher dioxide:",
                        size=f_normal,
                        width=280,
                        color=ft.colors.WHITE
                    ),
                    dropdown2
                ],
                alignment="center"
            ),
            Row(
                controls=[
                    Text(
                        "Risk in cleaning regime:",
                        size=f_normal,
                        width=280,
                        color=ft.colors.WHITE
                    ),
                    dropdown3
                ],
                alignment="center"
            ),
            Text(
                value="[M] Minimum distance from marine area.",
                size=f_normal,
                color=ft.colors.WHITE
            ),
            Text(
                value="[S] Minimum distance from salt source.",
                size=f_normal,
                color=ft.colors.WHITE
            ),
            Text(
                value="",
                size=2,
            ),
            TextButton(
                content=Text("Calculate suitable materials", size=f_normal*1.2),
                style=btn_style,
                width=400,
                on_click=lambda _: calculateMaterials(page, contents)
            ),
            Text(
                value="",
                size=7,
            ),
        ],
        horizontal_alignment="center",
    )
    
    page.update()

def calculateMaterials(page: Page, contents: Container):
    d1 = dropdown1.content.value
    d2 = dropdown2.content.value
    d3 = dropdown3.content.value
    
    if (d1 is None or d2 is None or d3 is None):
        alert(page)
        return
    
    f1, f2, f3 = 0, 0, 0
    for v in lst1:
        if (v[0] == d1):
            f1 = v[1]
            break
    for v in lst2:
        if (v[0] == d2):
            f2 = v[1]
            break
    for v in lst3:
        if (v[0] == d3):
            f3 = v[1]
            break

    materials = []
    i_crf = f1+f2+f3
    crf = "Corrosion Risk Factor (CRF) = " + str(i_crf)
    crc = ""
    clr = None
    
    if (i_crf == 1):
        crc = "Corrosion Risk Class (CRF) = I"
        materials = class1
        clr = "#014a08"
    elif (i_crf <= 0 and i_crf > -7):
        crc = "Corrosion Risk Class (CRF) = II"
        materials = class2
        clr = "#396601"
    elif (i_crf <= -7 and i_crf > -15):
        crc = "Corrosion Risk Class (CRF) = III"
        materials = class3
        clr = "#969400"
    elif (i_crf <= -15 and i_crf > -20):
        crc = "Corrosion Risk Class (CRF) = VI"
        materials = class4
        clr = "#874b01"
    else:
        crc = "Corrosion Risk Class (CRF) = V"
        materials = class5
        clr = "#870101"
    
    contents.content.controls.pop()

    output_mats = [
        Text(
            value="",
            size=7,
            weight="bold",
            color = ft.colors.WHITE,
        ),
        Text(
            value="Suitable materials",
            size=f_subheading,
            weight="bold",
            color = ft.colors.WHITE,
        ),
    ]
    for m in materials:
        output_mats.append(
            ft.ListTile(
                title=Text(
                    value=m,
                    size=f_normal,
                    color = ft.colors.WHITE,
                )
            )
            
        )

    contents.content.controls.append(
        Column(
            controls=[
                Divider(
                    thickness=1.5,
                    color=ft.colors.WHITE
                ),
                ft.Text(
                    value="Output",
                    color = ft.colors.WHITE,
                    size=f_subheading,
                    weight="bold",
                    text_align="center",
                ),
                Container(
                    content=Text(
                        value=crc,
                        size=f_normal,
                        text_align="center",
                        color=ft.colors.WHITE
                    ),
                    width=350,
                    padding=10,
                    border_radius = ft.border_radius.all(20),
                    bgcolor=clr,
                ),
                Container(
                    content=Text(
                        value=crf,
                        size=f_normal,
                        text_align="center",
                        color=ft.colors.WHITE
                    ),
                    width=350,
                    padding=10,
                    border_radius = ft.border_radius.all(20),
                    bgcolor=clr,
                ),
                Container(
                    content=ft.ListView(
                        controls=output_mats,
                    ),
                    width=800,
                    padding=10,
                    border_radius = ft.border_radius.all(20),
                    bgcolor=clr,
                ),
                
                Text(
                    value="",
                    size=2,
                ),
            ],
            horizontal_alignment="center",
        )
    )
    
    page.update()

def alert(page: Page):
    alert_str = "Please fill in all three dropdown boxes (F1, F2, and F3)."
    dlg = ft.AlertDialog(
        title=Text(
            value=alert_str,
            size=f_subheading/1.2,
        )
    )
    page.dialog = dlg
    dlg.open = True
    page.update()

def showEmail(page: Page):
    alert_str = "Email information:\n\nLucas Meyer: lucas.meyer77@gmail.com\nMichel Basson: michel@sassda.co.za"
    dlg = ft.AlertDialog(
        title=Text(
            value=alert_str,
            size=f_subheading/1.2,
        ),
    )
    page.dialog = dlg
    dlg.open = True
    page.update()

# --- RUN APP --- #

ft.app(
    view="web",
    target=initPage,
    assets_dir="assets"
)