import flet as ft
import os

__author__ = "Fatih AKMAN"
__status__ = "TEST"

"""
Script GUI de CARIBOU avec flet
Usage: uitest.py
"""


def main(page: ft.Page):
    # INITALISATION DES TABLEAUX
    def tableInit():
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        lv.controls.append(
            ft.ResponsiveRow(
                [
                    ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Last name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Age",weight=ft.FontWeight.BOLD,
                                                      ), numeric=True),
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
                                ft.DataColumn(ft.Text("First name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Last name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Age",weight=ft.FontWeight.BOLD,
                                                      ), numeric=True),
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
                    ),]), ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Last name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Age",weight=ft.FontWeight.BOLD,
                                                      ), numeric=True),
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
                    ),]), ft.Column(col={"sm": 6}, controls=[ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Last name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Age",weight=ft.FontWeight.BOLD,
                                                      ), numeric=True),
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
                                ft.DataColumn(ft.Text("First name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Last name",weight=ft.FontWeight.BOLD,
                                                      )),
                                ft.DataColumn(ft.Text("Age",weight=ft.FontWeight.BOLD,
                                                      ), numeric=True),
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

    # CHANGE LA VALEUR DU CONTROLLEUR QUI AFFICHE LE FICHIER SELECTIONNE
    def dropdown_changed(e):
        selectedFiletoString.value = f"Vous avez sélectionné le fichier : {dd.value}"
        page.update()
    # RETOURNE UNE LISTE DES FICHIERS PRESENT DANS '../files/'

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

    # INITALISATION APPBAR
    def appBarInit():
        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.DONUT_SMALL_OUTLINED),
            leading_width=40,
            title=ft.Text("CARIBOU V2"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
        )

    # INITALISATION BODY
    def bodyInit():
        page.add(ft.Container(
            content=ft.Text("Veuillez sélectionner un fichier"),
            padding=ft.Padding(6, 6, 0, 0),))

        selectedFileContainer = ft.Container(
            content=ft.Column([selectedFiletoString]),
            padding=ft.Padding(6, 0, 0, 0),
        )

        configContainer = ft.Container(
            content=ft.Column([ft.ResponsiveRow([
                ft.Column(col={"sm": 6}, controls=[dd]),
                ft.Column(col={"sm": 2}, controls=[ft.ElevatedButton(text="Export", color=ft.colors.BLACK),
                                                   ]),
                ft.Column(col={"sm": 2}, controls=[ft.ElevatedButton(text="Submit", color=ft.colors.BLACK)])])]),
            padding=6,
        )

        searchContainer = ft.Container(
            content=ft.TextField(label="Faire une recherche"),
            padding=6,
        )
        page.add(configContainer, selectedFileContainer, searchContainer)
        page.update()

    selectedFiletoString = ft.Text()
    fileOption = getFiles()

    dd = ft.Dropdown(
        on_change=dropdown_changed,
        options=fileOption,
        width=200,
    )

    appBarInit()
    bodyInit()
    tableInit()


# ENTRY POINT
if __name__ == "__main__":
    ft.app(target=main)
