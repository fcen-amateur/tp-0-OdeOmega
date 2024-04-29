import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder[["continent", "country"]].drop_duplicates(), x="continent")
        .add(so.Bar(), so.Hist())
        .label(
            title="Cantidad de países por continente",
            x="Continente",
            y="Cantidad de países",
        )
    )
    return dict(
        descripcion="Un test para ver si me sale el tp0",
        autor="OdeOmega",
        figura=figura,
    )
