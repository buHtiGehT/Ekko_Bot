#test file
import py_gg
py_gg.init("64b31aa6b110e5476cb84a4f7bea7afc")

champ = "Ahri"

mes = "{}".format(py_gg.stats.champion(champ))
print(mes)
