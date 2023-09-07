import flet as ft
import os

    

def main(page: ft.Page):

    
    def addTable():
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        lv.controls.append(
            ft.ResponsiveRow(
                [
                        ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name")),
                                ft.DataColumn(ft.Text("Last name")),
                                ft.DataColumn(ft.Text("Age"), numeric=True),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("John")),
                                        ft.DataCell(ft.Text("Smith")),
                                        ft.DataCell(ft.Text("43")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Jack")),
                                        ft.DataCell(ft.Text("Brown")),
                                        ft.DataCell(ft.Text("19")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Alice")),
                                        ft.DataCell(ft.Text("Wong")),
                                        ft.DataCell(ft.Text("25")),
                                    ],
                                ),
                            ],
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.CYAN,

                        border_radius=10,
                    ),]),

                    ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name")),
                                ft.DataColumn(ft.Text("Last name")),
                                ft.DataColumn(ft.Text("Age"), numeric=True),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("John")),
                                        ft.DataCell(ft.Text("Smith")),
                                        ft.DataCell(ft.Text("43")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Jack")),
                                        ft.DataCell(ft.Text("Brown")),
                                        ft.DataCell(ft.Text("19")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Alice")),
                                        ft.DataCell(ft.Text("Wong")),
                                        ft.DataCell(ft.Text("25")),
                                    ],
                                ),
                            ],
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.AMBER,

                        border_radius=10,
                    ),]),ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name")),
                                ft.DataColumn(ft.Text("Last name")),
                                ft.DataColumn(ft.Text("Age"), numeric=True),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("John")),
                                        ft.DataCell(ft.Text("Smith")),
                                        ft.DataCell(ft.Text("43")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Jack")),
                                        ft.DataCell(ft.Text("Brown")),
                                        ft.DataCell(ft.Text("19")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Alice")),
                                        ft.DataCell(ft.Text("Wong")),
                                        ft.DataCell(ft.Text("25")),
                                    ],
                                ),
                            ],
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.GREEN,

                        border_radius=10,
                    ),]),ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name")),
                                ft.DataColumn(ft.Text("Last name")),
                                ft.DataColumn(ft.Text("Age"), numeric=True),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("John")),
                                        ft.DataCell(ft.Text("Smith")),
                                        ft.DataCell(ft.Text("43")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Jack")),
                                        ft.DataCell(ft.Text("Brown")),
                                        ft.DataCell(ft.Text("19")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Alice")),
                                        ft.DataCell(ft.Text("Wong")),
                                        ft.DataCell(ft.Text("25")),
                                    ],
                                ),
                            ],
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.ORANGE,

                        border_radius=10,
                    ),]), ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name")),
                                ft.DataColumn(ft.Text("Last name")),
                                ft.DataColumn(ft.Text("Age"), numeric=True),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("John")),
                                        ft.DataCell(ft.Text("Smith")),
                                        ft.DataCell(ft.Text("43")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Jack")),
                                        ft.DataCell(ft.Text("Brown")),
                                        ft.DataCell(ft.Text("19")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Alice")),
                                        ft.DataCell(ft.Text("Wong")),
                                        ft.DataCell(ft.Text("25")),
                                    ],
                                ),
                            ],
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.PINK,

                        border_radius=10,
                    ),]),
                ]))
        page.add(lv)
        page.update()

    
    def dropdown_changed(e):
        t.value = f"Vous avez sélectionné le fichier : {dd.value}"
        page.update()
    
    def getFiles():
        fileSet = set()
        for root, dirs, files in os.walk('files'):
            for fileName in files:
                fileSet.add(os.path.join(root[len('files'):], fileName))

        print(fileSet)
        fileOption = []
        for file in files:
            fileOption.append(ft.PopupMenuItem(text=file))
        fileOption.append(ft.PopupMenuItem())
        return fileOption
    
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.DONUT_SMALL_OUTLINED),
        leading_width=40,
        title=ft.Text("CARIBOU V2"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,

    )
    t = ft.Text()
    t.value = "Veuillez sélectionner un fichier"
    page.add(t)
    fileOption = getFiles()
    dd = ft.Dropdown(
            on_change=dropdown_changed,
            options=fileOption,
            width=200,
    )
    t = ft.Text()
    c1 = ft.Container(
        content=ft.Column([t,dd]),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )
   


    conf = ft.ResponsiveRow(  [
        ft.Column(col={"sm": 6}, controls=[dd]),
                ft.Column(col={"sm": 2}, controls=[        ft.ElevatedButton(text="Submit",color=ft.colors.BLACK),
]),
                ft.Column(col={"sm": 2}, controls=[        ft.ElevatedButton(text="Submit",color=ft.colors.BLACK)

    ])])

    
    page.add(conf, t)
    nameinput = ft.TextField(label="Search name",
		)
    page.add(nameinput)
    

    page.title = "CARIBOU"

    page.update()
    addTable()
    

ft.app(target=main)
