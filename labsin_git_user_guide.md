# Git 

En el LABSIN usamos un metodologia de trabajo que se apoya fuertemente en [github](https://github.com) (o eventualmente [gitlab](https://gitlab.com)). [Git](https://git-scm.com/) es un sistema de control de versiones que permite llevar cuenta de los cambios hechos en el codigo fuente.

A diferencia de CVS, SVN o TFS (el de microsoft), `git` un sistema de control de versiones  distribuido: es decir, hay un repo llamado "origin", que es como el punto donde eventualmente se centraliza y sincroniza el trabajo de todos, pero luego cada uno tiene un repo local (al menos). Por eso es que primero se commitean los cambios (a tu repo local), y luego se hace push para mandar esos cambios.


### Github

Github es un sitio

### El workflow
La idea es basicamente seguir el [github worflow](http://https://docs.github.com/en/get-started/quickstart/github-flow "worflow")

Aca va un breve resumen

1. Se trabaja jerarquicamente con 2 branches (que pueden ir en paralelo)
`master`: Producción
`develop`: Branch de integración de todos los desarrollos 

2. Para cada nueva feature se usan los topic branches:  Estos deberian crearse siempre desde develop:
a) `git checkout develop`  (te pasas al branch develop)
b)  `git pull origin develop`  (te traes lo ultimo del repo origin)
c)  `git checkout -b feature/<nombre-descriptivo-de-mi-feature> develop` (crea un nuevo branch a partir de develop y se pasa a ese nuevo branch) 
d) Se hace el trabajo en el branch
d) `git commit -am ".... <comentario descriptivo de lo que hiciste...>"`  (Se commitean los cambios en tu repo local). En el comentario se puede linkear al issue usando #numero de issue
e)`git push origin feature/<nombre....> ` (manda el branch a `origin`, creandolo si no existe o actualizandolo si existe)
f) Lue se crea el PR (Pull Request) desde el sitio de github y se esperan los comentarios de los demas.
g) Cuando se apruebe el PR se puede hacer el merge

Despues, si alguien crea un branch y lo pushea a `origin`, y vos queres bajartelo a tu repo local, haces primero `git fetch origin`,  y después podés hacer `git checkout <branch>`  o alternativamente haces `git checkout --track origin/<branch>`


 ### Sobre las releases
Cuando se va a hacer una release, se hace tipicamente un solo PR desde `develop` a `master`, revisas y mergeas en `master`. 

Luego para mantener el historial de versiones se suelen agregar tags en `master` (podes agregarlos en cualquier branch igualmente si te sirven). Los tags son como marcadores en el historial y luego de ser necesario podes crear branches off of those tags.

### Comandos utiles
#### Eliminar N commits
`git reset --hard HEAD~2` mueve el branch actual hacia atrás dos commits

