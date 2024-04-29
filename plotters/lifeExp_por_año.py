import seaborn.objects as so
from gapminder import gapminder

evolucionExp = gapminder.groupby(["year", "continent"])["lifeExp"].mean().reset_index()

def plot():
    figura = (
        so.Plot(data = evolucionExp, x="year", y="lifeExp")
        .add(so.Line(), color="continent")
        .add(so.Dot(), color="continent")
        .label(
            title="Evolución de la expectativa de vida",
            x="Año",
            y="Expectatica de vida",
        )
        
    )
    
    return dict(
        descripcion="Evolución de expectativa de vida por continente",
        autor="OdeOmega",
        figura=figura,
    )
