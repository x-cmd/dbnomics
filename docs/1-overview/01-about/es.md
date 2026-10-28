# Economía que se puede ver

Cada gráfico de este sitio es un enlace. Ábrelo y aparece la imagen; lee el enlace y obtienes los números que hay detrás: los datos viven dentro de la URL, así que un agente de IA también puede leerlos. Los temas son los que deciden cómo se te va la semana: empleo, precios, crecimiento, deuda y qué están haciendo realmente las mayores economías del planeta.

El sitio se organiza en seis secciones que se leen en una sola dirección: **qué mirar → qué regla lo ata → cómo se ve de cerca una economía**. Indicadores (PIB, crecimiento, inflación, desempleo, deuda, el saldo con el exterior, cuenta corriente, tipos oficiales, población y ahorro) · macroeconomía (cinco leyes: Phillips, Okun, Wagner, Beveridge, Laffer) · y tres estudios de caso: Europa, Estados Unidos y China.

¿No sabes por dónde empezar? Estas seis páginas son las que se discuten — y cada una responde una pregunta que ya te hacías.

**Tres economías, tres argumentos.** Estados Unidos, la zona euro y China en los mismos indicadores: qué mercado laboral está más tenso, qué precios están más tranquilos, quién sigue creciendo, quién pide prestado más. Todo el mundo tiene una opinión; aquí están los datos — y los puntos donde los datos se niegan a zanjar la discusión.

**Tu empleo y tu cesta de la compra están en el mismo balancín.** La curva de Phillips es la regla más antigua de la macroeconomía: cuando los precios suben, los empleos escasean, así que los gobiernos tienen que elegir cuál de los dos quieren más. Estados Unidos acaba de recorrer la versión más suave en cuarenta años.

**¿Cómo puede una ciudad tener empleos que nadie quiere y personas que necesitan uno?** La curva de Beveridge traza las vacantes frente al desempleo. Normalmente baja; la pandemia la dobló hacia fuera y desde entonces no ha vuelto a enderezarse del todo.

**El único indicador que ha anticipado todas las recesiones estadounidenses en sesenta años.** Cuando el rendimiento del Treasury a 10 años cae por debajo del de 3 meses, el mercado apuesta a que el banco central va a recortar — y suele seguir una recesión. Se invirtió en 2022 y 2023; en 2025 volvió a empinarse.

**Cincuenta economías, una sola tarjeta de crédito.** Washington aplica una única política fiscal, un único mapa de la Reserva Federal y un único tribunal de quiebras a estados que comparten una moneda y casi nada más. Nueva York y Misisipi están a un factor 2,2 de distancia, y 24 años de «convergencia» no lo cerraron.

**Un país, dos economías.** En la costa china una ciudad fabril puede ganar más que toda una provincia del norte. La brecha se redujo de 11,7 veces a 4,3 — pero la gente fue en la dirección contraria: Guangdong tiene 55 millones de habitantes más que en 2000.

Cómo leer un gráfico aquí: haz clic en él. La URL *es* el gráfico, y los números están a la vista dentro de ella. Los datos están a una orden de distancia (ayuda del módulo: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth
x dbnomics align imf.us.gdp imf.cn.gdp
x dbnomics alias
```

Vintage de los datos: el *World Economic Outlook* del FMI (edición de 2025, con pronósticos) y los tipos oficiales del BPI; las páginas de estados y provincias usan la base de datos regional de la OCDE. Cada gráfico usa 2025 como su último año. **Inicio rápido**: pega la URL de cualquier gráfico en un documento, o apunta a un agente de IA con el [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) y pídele que represente el PIB de Estados Unidos frente al de China.
