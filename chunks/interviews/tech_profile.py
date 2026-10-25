"""As 70 perguntas mais comuns em entrevistas em inglês, respondidas com o perfil do Igor.

A lista de perguntas segue as mais frequentes em entrevistas de emprego
(apresentação, carreira, jeito de trabalhar, equipe, pressão, condições e
encerramento). As respostas são originais e usam a trajetória real em
tecnologia: Data Analyst numa refinaria (Python, SAP, dashboards) e fundador
da PGBA Solutions (Django, FastAPI, React, TypeScript, PostgreSQL).

Serve para qualquer vaga de tecnologia: troque os ((preencha)) pelos seus fatos.
"""

from chunks.interviews import Question, Session, Stage, register

Q = Question

STAGES = (
    Stage(
        "intro",
        "Abertura e apresentação",
        "Os primeiros minutos: inglês, pitch, formação. Aqui se forma a primeira impressão.",
    ),
    Stage(
        "background",
        "Experiência e requisitos",
        "O que você já fez, o que te falta e por que está saindo. Fatos, não adjetivos.",
    ),
    Stage(
        "stories",
        "Histórias (STAR)",
        "Desafios, falhas e sucessos. Prepare 5 histórias reais e reaproveite: "
        "Situation, Task, Action, Result.",
    ),
    Stage(
        "career",
        "Carreira e motivação",
        "Para onde você vai, por que tecnologia e por que esta empresa.",
    ),
    Stage(
        "style",
        "Jeito de trabalhar",
        "Rotina, organização, pressão, estresse e mudanças. Querem previsibilidade.",
    ),
    Stage(
        "team",
        "Equipe e liderança",
        "Colaboração, conflitos, delegar e liderar. Mostre maturidade, nunca reclame de ninguém.",
    ),
    Stage(
        "personal",
        "Valores e pessoal",
        "Perguntas abertas sobre você. Respostas curtas, honestas e que voltem para o trabalho.",
    ),
    Stage(
        "conditions",
        "Condições",
        "Horas, viagens, mudança, salário e início. Seja honesto e não feche valor cedo demais.",
    ),
    Stage(
        "closing",
        "Suas perguntas",
        "Sempre tenha perguntas prontas. Elas mostram que você fez a lição de casa.",
    ),
)

QUESTIONS = (
    # ------------------------------------------------------------- abertura
    Q(
        "english_ok",
        "intro",
        "Do you mind if we do this interview in English?",
        "Se você trava ou aceita com tranquilidade. A resposta já é o primeiro teste de inglês.",
        "[[Not at all]], I'd be happy to. I use English every day for documentation and code, "
        "[[so it's a great chance to practice]]. "
        "[[If I don't understand something, I'll ask you to rephrase it.]]",
        tips=(
            "Sorria e responda rápido. Hesitar aqui passa insegurança.",
            "Já deixe combinado que vai pedir para repetir quando precisar.",
        ),
    ),
    Q(
        "english_level",
        "intro",
        "How would you rate your English?",
        "Se a sua autoavaliação é realista. Exagerar ou se diminuir demais pega mal.",
        "[[I'd say]] my English is ((intermediate to advanced)). Reading and writing are strong, "
        "because I work with technical documentation, Stack Overflow and code reviews in English "
        "every day. Speaking is [[what I've been working on the most]], ((with daily practice and "
        "conversation classes)). [[I can handle]] technical discussions comfortably, "
        "and I keep getting better.",
        tips=(
            "Separe as habilidades: leitura, escrita, conversa. Fica mais crível.",
            "Mostre que você está melhorando (o que faz para isso).",
        ),
    ),
    Q(
        "about_yourself",
        "intro",
        "Tell me a little bit about yourself.",
        "Seu pitch de 60 a 90 segundos: quem você é profissionalmente e por que está aqui.",
        "Sure! I'm Igor, [[I'm a]] software developer and data analyst from Brazil. "
        "[[I've been working in]] tech and data [[for]] ((about six years)). "
        "[[I currently work as]] a Data Analyst ((at an oil refinery)), "
        "[[where I'm responsible for]] Python data pipelines and dashboards built on SAP data. "
        "In parallel, I founded PGBA Solutions, [[where I build]] web products end to end with "
        "Django, FastAPI, React, TypeScript and PostgreSQL. "
        "[[What I enjoy most is]] turning messy data into tools people actually use, "
        "[[and that's why this role caught my attention]].",
        tips=(
            "Presente → passado → futuro → ligação com a vaga.",
            "Ensaie até sair sem ler. Grave no celular e ouça.",
            "Não fale de família, idade ou hobbies aqui, a não ser que perguntem.",
        ),
        follow_ups=("What does PGBA do?", "Which technology do you use the most?"),
    ),
    Q(
        "background",
        "intro",
        "What's your background?",
        "Formação e caminho até a tecnologia. Querem entender a sua história em ordem.",
        "[[My background is in]] ((your degree)). [[I started my career in]] ((first area)), "
        "and [[that's where I discovered]] programming: I started automating reports with Python "
        "and never stopped. "
        "[[Since then]], I've moved more and more into software development: first data "
        "pipelines and dashboards, and later full web applications at my own company.",
        tips=("Conte como uma linha do tempo curta, com uma virada clara.",),
    ),
    Q(
        "graduation",
        "intro",
        "What did you graduate in?",
        "Pergunta direta. Responda o curso, a instituição e o ano, e ligue com o seu trabalho.",
        "[[I graduated in]] ((your course)) [[from]] ((university)) [[in]] ((year)). "
        "[[On top of that]], I've taken courses in ((Python, data engineering, cloud)), "
        "because most of what I use today I learned by building real projects.",
        tips=("Se a formação não for em computação, mostre o que estudou depois.",),
    ),
    # ----------------------------------------------- experiência e requisitos
    Q(
        "tools",
        "background",
        "What tools and technologies are you most experienced with?",
        "A versão de tecnologia do 'você sabe Excel?'. Querem saber o que você domina de verdade.",
        "[[My main stack is]] Python: pandas for data, Django and FastAPI for backends. "
        "On the frontend, React with TypeScript. For databases, mostly PostgreSQL, and I write "
        "a lot of SQL. [[I'm also comfortable with]] Git, Docker, Power BI and of course Excel, "
        "which is everywhere at the refinery. "
        "[[I'm less experienced with]] ((a tool from the job description)), "
        "but I pick up new tools quickly.",
        tips=("Separe o que você domina do que já usou. Nunca liste o que não sustenta.",),
    ),
    Q(
        "sales",
        "background",
        "Do you have any experience dealing with clients or sales?",
        "Comunicação com cliente e visão de negócio, importante para quem tem empresa própria.",
        "Yes, through PGBA. [[As a founder, I've been the one]] talking to clients, understanding "
        "their problem, writing proposals and negotiating scope. "
        "[[It taught me to]] explain technical decisions in business terms, "
        "which helps a lot when working with product people.",
        tips=("Transforme a PGBA em prova de comunicação e de visão de produto.",),
    ),
    Q(
        "requirements",
        "background",
        "After reading the job description, do you think you meet all the requirements? "
        "Which ones would you need to improve?",
        "Honestidade e autoconhecimento. Ninguém cumpre 100%; querem ver como você fecha a lacuna.",
        "[[I meet most of them]]: Python, APIs, SQL and working with data from different sources "
        "are things I do every day. "
        "[[Where I'd need to ramp up is]] ((one requirement, e.g. Kubernetes)). "
        "[[What I'm doing about it is]] ((a course or side project)), "
        "and [[I've done that before]]: I learned FastAPI by shipping a real project with it.",
        tips=(
            "Cite uma lacuna real e o que você já está fazendo para fechá-la.",
            "Nunca diga 'I have all of them' sem poder provar.",
        ),
    ),
    Q(
        "visa",
        "background",
        "Do you have a work visa, or would you need sponsorship?",
        "Questão prática para vagas no exterior. Para vagas remotas, explique como funciona.",
        "((For remote roles:)) I'd work remotely from Brazil as a contractor, "
        "[[so I wouldn't need a visa]]. ((If the role is on-site: I don't have a visa yet, "
        "so I'd need sponsorship / I have a ... visa.))",
        tips=("Responda direto. Se precisar de patrocínio, diga sem rodeios.",),
    ),
    Q(
        "why_leave_current",
        "background",
        "Why do you want to leave your current job?",
        "Se há problema (conflito, demissão) e se você vai ficar. Querem uma motivação positiva.",
        "[[To be honest]], I'm not running away from anything. I've learned a lot at the refinery, "
        "but data analysis is only part of what I want to do. "
        "[[I'm looking to]] work full-time on software products, with a strong engineering team "
        "and in an international environment. "
        "[[This role is the natural next step for that.]]",
        tips=("Fale do que você busca, nunca do que você quer evitar.",),
    ),
    Q(
        "why_left_last",
        "background",
        "Why did you leave your last job?",
        "Igual à anterior, mas sobre o passado. Uma frase clara e positiva basta.",
        "((I left ... because ...)). [[It was a good place to learn]], but [[I wanted to]] "
        "((grow / work more with code / take on more responsibility)), "
        "and the move to ((next job)) gave me exactly that.",
        tips=("Se foi demitido, diga com calma, em uma frase, e foque no que aprendeu.",),
    ),
    Q(
        "responsibilities",
        "background",
        "What are your main responsibilities in your current position?",
        "O dia a dia real e o tamanho do seu escopo. Verbos de ação e resultados.",
        "At the refinery, [[I'm responsible for]] three main things. First, building Python "
        "pipelines that extract and clean data from SAP and spreadsheets. Second, creating "
        "dashboards that ((operations / management)) use to make decisions. Third, automating "
        "manual reports, which ((saved the team X hours a week)). "
        "At PGBA, [[I own the whole cycle]]: from the first conversation with the client "
        "to deploying and maintaining the product.",
        tips=("Três responsabilidades com verbos fortes: build, automate, own.",),
    ),
    Q(
        "fired_someone",
        "background",
        "Have you ever had to let someone go? How did you feel about it?",
        "Maturidade em decisões difíceis. Se nunca aconteceu, diga e mostre como faria.",
        "((If yes: At PGBA, I had to end a contract with a freelancer who ... It wasn't easy, "
        "but ...)). ((If no:)) [[I haven't had to do that so far]], but I've given difficult "
        "feedback. [[I believe]] the key is to be clear early, so it's never a surprise, "
        "and to treat the person with respect.",
    ),
    # ------------------------------------------------------------- histórias
    Q(
        "new_task",
        "stories",
        "Tell me about a time you faced a completely new task. How did you deal with it? "
        "What was the outcome?",
        "Como você aprende sob demanda. A melhor resposta mostra método, não sorte.",
        "[[The situation was that]] ((a PGBA client needed a feature with a technology I had "
        "never used, e.g. payments / maps / FastAPI)). "
        "[[My task was to]] deliver it in ((two weeks)). "
        "[[What I did was]] read the official docs first, build a tiny proof of concept, "
        "and only then plug it into the product, with tests around it. "
        "[[As a result]], ((we delivered on time and the client ...)). "
        "[[What I learned was]] that a small prototype saves a lot of time.",
        tips=("Mostre o método: estudar, prototipar, integrar, testar.",),
    ),
    Q(
        "biggest_failure",
        "stories",
        "What was your biggest failure at work, and what did you learn from it?",
        "Autocrítica. Fugir da pergunta ('sou perfeccionista') é a pior resposta.",
        "((A real failure: e.g. I underestimated a PGBA project and missed the deadline by three "
        "weeks)). [[To be honest]], it was my fault: ((I didn't break the scope down)). "
        "I told the client early, renegotiated the scope and delivered the most important part "
        "first. [[What I learned was]] to split work into small deliveries and estimate "
        "with a margin. [[Since then]], ((what you do differently)).",
        tips=("Escolha um erro real, já resolvido, e gaste mais tempo no aprendizado.",),
    ),
    Q(
        "didnt_like",
        "stories",
        "Tell me something you didn't like about your last job.",
        "Armadilha: querem ver se você fala mal da empresa. Escolha algo neutro e construtivo.",
        "[[If I had to pick one thing]], it would be the amount of manual work in some processes, "
        "like reports built by hand every week. "
        "[[But instead of just complaining]], I automated a few of them with Python, "
        "[[and that's actually how]] I got more involved with software.",
        tips=("Nunca critique pessoas. Critique um processo e mostre o que você fez.",),
    ),
    Q(
        "biggest_challenge",
        "stories",
        "Describe the biggest challenge you've had at work and how you handled it.",
        "Sua história técnica mais forte, em formato STAR.",
        "[[The biggest challenge was]] ((consolidating data from SAP and dozens of spreadsheets "
        "into one reliable dataset)). The same items had different names, codes and formats. "
        "[[What I did was]] build a Python pipeline that standardized the fields, removed "
        "duplicates, and flagged bad records for review instead of silently fixing them. "
        "[[As a result]], ((the monthly report went from X days to Y hours)), "
        "and people started trusting the numbers.",
        tips=("Tenha números reais. Sem números a história perde metade da força.",),
    ),
    Q(
        "did_well",
        "stories",
        "Give me an example of something you did really well at work.",
        "Um resultado concreto e o seu papel nele.",
        "[[One thing I'm proud of is]] ((an automation at the refinery)). "
        "Every week, ((someone spent a whole day)) copying data into a report. "
        "I built a script that did it in ((minutes)) and added checks to catch inconsistent data. "
        "[[It saved the team]] ((hours per month)), and [[it ended up being used by]] "
        "((other areas)).",
    ),
    Q(
        "successful_projects",
        "stories",
        "What are the most successful projects you've worked on?",
        "Projetos com impacto. Escolha um ou dois e conte o problema, a solução e o resultado.",
        "[[I'd highlight two]]. The first is ((a PGBA product)): a web platform with a Django or "
        "FastAPI backend, React frontend and PostgreSQL, [[that's now used by]] ((N users / "
        "clients)). [[I designed it end to end]], from the data model to the deploy. "
        "The second is ((the data pipeline at the refinery)), which ((result)). "
        "[[Both of them taught me]] to always start from the user's problem.",
        follow_ups=(
            "What was the hardest technical decision in that project?",
            "What would you do differently today?",
        ),
    ),
    # ---------------------------------------------------- carreira e motivação
    Q(
        "important_company",
        "career",
        "What's important to you in a company?",
        "Se os seus valores combinam com os deles.",
        "[[For me, the most important thing is]] a team that cares about quality: code reviews, "
        "tests and honest feedback. "
        "[[I also value]] autonomy with clear goals, and a culture where it's okay to ask questions. "
        "[[That's the kind of place where]] I do my best work.",
        tips=("Pesquise os valores da empresa e cite um que combine com o seu.",),
    ),
    Q(
        "why_this_company",
        "career",
        "Why would you like to work for us? What do you know about our company?",
        "Se você pesquisou. Resposta genérica elimina candidatos.",
        "[[I've been reading about]] ((the company: product, mission, recent news)), "
        "and [[what caught my attention]] was ((a concrete detail)). "
        "[[On top of that]], the role [[is a great match for]] my experience with "
        "((Python / data / APIs)). [[I believe I could contribute]] to ((a specific challenge)) "
        "from the beginning.",
        tips=(
            "Leia o site, o LinkedIn, o blog técnico e o GitHub da empresa antes.",
            "Cite produto, clientes ou stack. 'É uma ótima empresa' não conta.",
        ),
    ),
    Q(
        "other_opportunities",
        "career",
        "Are you applying for other jobs?",
        "Urgência e concorrência. Não precisa dar nomes.",
        "((Answer honestly: 'Yes, I'm in early conversations with a couple of companies' or "
        "'Not actively')). [[But this role is at the top of my list]], "
        "because it matches what I do best.",
    ),
    Q(
        "looking_for",
        "career",
        "What are you looking for in a job?",
        "Se o que você quer existe nesta vaga.",
        "[[I'm looking for]] three things: challenging technical problems, especially with data and "
        "APIs; a strong team I can learn from; and real ownership, being involved from the idea "
        "to production. [[From what I've seen]], this role has all three.",
    ),
    Q(
        "future_courses",
        "career",
        "What courses or skills are you planning to study next?",
        "Se você investe na própria carreira e se o plano faz sentido para a vaga.",
        "[[Right now I'm focused on]] two things: my spoken English, ((with daily practice)), "
        "and ((cloud: an AWS or Azure certification)). "
        "[[Next, I'd like to]] go deeper into ((system design / data engineering)), "
        "because it's where I see the biggest impact in the kind of products I build.",
        tips=("Cite algo que você já começou. Plano sem ação não convence.",),
    ),
    Q(
        "career_goals",
        "career",
        "What are your short-term and long-term career goals?",
        "Se você tem direção e se ela cabe na empresa.",
        "[[In the short term]], [[I want to]] join a strong engineering team, deliver well and "
        "become a reference in ((Python and data)). "
        "[[In the long term]], [[I see myself]] as a senior or staff engineer, designing systems "
        "and helping other developers grow.",
    ),
    Q(
        "five_years",
        "career",
        "Where do you see yourself in five years?",
        "Ambição realista e se você pretende ficar.",
        "[[In five years, I see myself]] as a senior engineer who owns important parts of the "
        "product, and [[ideally]] still at this company, growing with it. "
        "I'd like to be the person people come to for ((data and backend)) questions, "
        "and [[to be mentoring]] newer developers.",
        tips=("Não diga que quer abrir a sua empresa ou o cargo do entrevistador.",),
    ),
    Q(
        "satisfied_career",
        "career",
        "Are you satisfied with your career so far?",
        "Equilíbrio: orgulho do caminho e vontade de crescer.",
        "[[Overall, yes]]. I built a solid base in data and I've shipped real products at PGBA. "
        "[[But I'm not done]]: the next step is working on larger products with a bigger team, "
        "[[which is exactly why I'm here]].",
    ),
    Q(
        "why_tech",
        "career",
        "Why did you choose a career in technology?",
        "A motivação real. Uma história curta e verdadeira vale mais que um discurso.",
        "[[It started when]] ((I automated my first report with Python)). Seeing a task that took "
        "a day run in seconds was addictive. "
        "[[What keeps me here is]] that every problem is different, and I'm always learning. "
        "I like that software has a real, visible impact on people's work.",
    ),
    Q(
        "continuous_improvement",
        "career",
        "How do you keep improving professionally? Are you seeing results?",
        "Disciplina de aprendizado contínuo, com provas.",
        "[[I learn mostly by building]]. Every new PGBA project is a chance to try something, "
        "like ((FastAPI or TypeScript)). [[On top of that]], I read documentation and engineering "
        "blogs, and ((take courses)). "
        "[[And yes, I'm seeing results]]: ((one concrete result, e.g. I moved from scripts to "
        "full web applications in two years)).",
    ),
    Q(
        "successful",
        "career",
        "Do you consider yourself successful?",
        "Autoconfiança sem arrogância.",
        "[[In many ways, yes]]. I built a career in tech, founded a company, and my work is used "
        "by real people every day. "
        "[[But for me, success is a direction, not a destination]]: I still have a lot to learn.",
    ),
    Q(
        "dream_job",
        "career",
        "What's your dream job?",
        "Se a vaga se aproxima do que você quer. Descreva características, não um cargo em outra empresa.",
        "[[My dream job is]] one where I solve real problems with data and code, on a product "
        "people depend on, with a team that pushes me to be better. "
        "[[Honestly, this role is very close to that.]]",
    ),
    # --------------------------------------------------------- jeito de trabalhar
    Q(
        "routine",
        "style",
        "What's your typical work routine? How do you organize yourself?",
        "Organização e previsibilidade, ainda mais em trabalho remoto.",
        "[[I usually start the day by]] checking messages and reviewing my priorities. "
        "[[Then I block]] the morning for focused work, like coding or data analysis, "
        "with notifications off. Meetings and code reviews go to the afternoon. "
        "I track tasks in ((Trello / Jira / Notion)), and at the end of the day "
        "[[I write down]] where I stopped, so the next day starts fast.",
    ),
    Q(
        "favorite_task",
        "style",
        "You do many different tasks at work. Which one do you like the most?",
        "O que te dá energia. Ideal se coincidir com o centro da vaga.",
        "[[What I enjoy the most is]] designing the solution: modeling the data, deciding how the "
        "API should look, and then seeing it work end to end. "
        "[[I also really like]] debugging hard problems. Finding the root cause is very satisfying.",
    ),
    Q(
        "boring_tasks",
        "style",
        "Do you find any work activities boring?",
        "Armadilha: querem ver se você evita trabalho necessário.",
        "[[Every job has repetitive tasks]], like filling in reports or manual checks. "
        "[[But I see them as]] candidates for automation. Many of my best scripts started "
        "because something was boring. "
        "[[And when it can't be automated]], I just do it well and move on.",
    ),
    Q(
        "environment",
        "style",
        "What kind of work environment are you most comfortable in?",
        "Encaixe com a cultura (remoto, ritmo, autonomia).",
        "[[I'm most comfortable in]] an environment with clear goals and autonomy to reach them. "
        "I've been working remotely ((for years)), so [[I'm used to]] written communication and "
        "async work. [[I also like]] teams where people share knowledge openly.",
    ),
    Q(
        "strengths_weaknesses",
        "style",
        "What are your strengths and weaknesses?",
        "Autoconhecimento. Uma força com prova e uma fraqueza real com plano.",
        "[[I'd say my main strength is]] turning messy problems into working solutions. "
        "[[For instance]], ((the SAP data pipeline)). "
        "[[As for weaknesses]], I sometimes try to solve everything myself before asking for help, "
        "probably because of years running my own company. "
        "[[I've been working on that]] by setting a time limit: if I'm stuck for "
        "((an hour)), I ask.",
        tips=("A fraqueza tem que ser real e não pode ser essencial para a vaga.",),
    ),
    Q(
        "describe_boss",
        "style",
        "How would you describe your current or previous boss?",
        "Armadilha: nunca fale mal. Querem ver como você se relaciona com a hierarquia.",
        "((My manager)) [[is very results-oriented]] and gives me a lot of autonomy. "
        "[[What I learned from them is]] ((to always connect the data to a business decision)). "
        "[[We have a good relationship]], with honest feedback in both directions.",
        tips=("Mesmo que o chefe seja ruim, fale de algo que você aprendeu.",),
    ),
    Q(
        "others_describe",
        "style",
        "How would your boss and coworkers describe you?",
        "Como você é visto. Use palavras que outras pessoas realmente usaram.",
        "[[I think they'd say]] I'm reliable and the person who gets things done. "
        "((In my last feedback, my manager said ...)). "
        "[[My coworkers would probably add that]] I'm always willing to help, "
        "especially with Python and data problems.",
        tips=("Se tiver um feedback real ou recomendação no LinkedIn, cite.",),
    ),
    Q(
        "workaholic",
        "style",
        "Do you consider yourself a workaholic?",
        "Comprometimento x equilíbrio. O ideal é o meio-termo.",
        "[[Not really]]. I'm very committed, and when there's an urgent issue I stay until it's "
        "solved. [[But I believe]] rest is part of doing good work: a tired developer writes bugs. "
        "[[So I try to keep]] a healthy balance.",
    ),
    Q(
        "under_pressure",
        "style",
        "How do you work under pressure?",
        "Se você mantém a qualidade e a comunicação quando aperta.",
        "[[I stay calm and get organized]]. I break the problem into smaller pieces, "
        "[[deal with the most critical part first]], and keep people updated. "
        "[[For example]], ((a production issue at PGBA with a client waiting)): ((what you did)). "
        "[[Pressure actually helps me focus]].",
    ),
    Q(
        "stress",
        "style",
        "How do you handle stress?",
        "Se você tem estratégias saudáveis.",
        "At work, [[I handle stress by]] organizing: writing everything down and talking to the "
        "team early when something is at risk. Outside work, ((exercise / time with family)) "
        "[[helps me recharge]].",
    ),
    Q(
        "change",
        "style",
        "How do you deal with change at work?",
        "Adaptabilidade. Tecnologia muda o tempo todo.",
        "[[I see change as part of the job]], especially in tech. "
        "[[When priorities change]], I try to understand the reason behind the decision, "
        "and then adapt quickly. "
        "[[At PGBA, for example]], ((a client changed the scope mid-project, and ...)).",
    ),
    Q(
        "out_of_the_box",
        "style",
        "Can you think outside the box?",
        "Criatividade com exemplo, não só 'sim'.",
        "[[I'd like to think so]]. [[For example]], ((instead of building a full system for a "
        "client, I suggested a simple spreadsheet integration that solved 80% of the problem in "
        "a week)). [[Sometimes the creative solution is the simplest one.]]",
    ),
    Q(
        "difficult_decisions",
        "style",
        "In your opinion, what are the hardest decisions to make?",
        "Como você raciocina sobre trade-offs.",
        "[[For me, the hardest decisions are]] the ones with trade-offs and incomplete "
        "information, like ((shipping now with technical debt or delaying to do it right)). "
        "[[What helps me is]] making the trade-offs explicit, talking to the people affected, "
        "and choosing an option that's easy to revisit.",
    ),
    Q(
        "after_pandemic",
        "style",
        "How has the way you work changed after the pandemic?",
        "Adaptação ao trabalho remoto e híbrido.",
        "[[The biggest change was]] remote work. [[I learned to]] communicate much more in writing, "
        "document decisions and work with people in different places. "
        "[[It also showed me]] that I'm very productive working remotely, "
        "((which is why I'm looking for remote roles)).",
    ),
    # -------------------------------------------------------- equipe e liderança
    Q(
        "team_player",
        "team",
        "Are you a team player?",
        "Colaboração com exemplo concreto.",
        "Yes. [[I enjoy working with others]], and I think software is a team sport: code reviews, "
        "pair programming and sharing knowledge make the product better. "
        "[[For example]], ((I created a small Python guide for my team at the refinery so they "
        "could run the reports themselves)).",
    ),
    Q(
        "delegate",
        "team",
        "Are you able to delegate work?",
        "Confiança nos outros e capacidade de não centralizar.",
        "Yes, [[I've learned to]], mostly at PGBA. At first I tried to do everything myself, "
        "[[but that doesn't scale]]. Now I give context, define what 'done' looks like, "
        "and stay available for questions, [[without micromanaging]].",
    ),
    Q(
        "own_decisions",
        "team",
        "Are you able to make decisions on your own?",
        "Autonomia com responsabilidade.",
        "Yes. [[Running my own company taught me to]] make decisions with the information I have. "
        "[[For small, reversible decisions]], I decide and move on. "
        "[[For big ones]], like architecture or anything that affects clients, "
        "I gather input first and document the reasons.",
    ),
    Q(
        "leader_follower",
        "team",
        "Are you more of a leader or a follower?",
        "Flexibilidade. A melhor resposta: depende do contexto.",
        "[[It depends on the situation]]. When I know the subject well, like data pipelines, "
        "[[I naturally take the lead]]. When someone else has more experience, "
        "[[I'm happy to follow]] and learn. [[What matters is]] that the team delivers.",
    ),
    Q(
        "lead_people",
        "team",
        "Do you usually lead people at work? How do you get along with them?",
        "Experiência real de liderança, mesmo informal.",
        "((At PGBA, I coordinate freelancers / a small team)). [[I try to lead by example]]: "
        "being clear about priorities and reviewing work with respect. "
        "[[We get along well]], because I listen and I give credit to the people who did the work.",
    ),
    Q(
        "good_leader",
        "team",
        "Do you consider yourself a good leader?",
        "Humildade com evidência.",
        "[[I'm still learning]], but I think I have good foundations: I communicate clearly, "
        "I'm fair, and I care about people growing. "
        "((The freelancers I've worked with keep coming back to work with me)), "
        "[[which I take as a good sign]].",
    ),
    Q(
        "leader_qualities",
        "team",
        "What qualities make a good leader?",
        "Sua visão de liderança.",
        "[[In my opinion]], a good leader gives clear direction, removes obstacles for the team, "
        "and is honest, even when the news is bad. "
        "[[Above all]], a good leader makes other people better. "
        "[[In tech]], that also means protecting the team's time to focus.",
    ),
    Q(
        "irritates",
        "team",
        "What irritates you about coworkers?",
        "Armadilha: não reclame. Mostre como você lida com o incômodo.",
        "[[I don't get irritated easily]]. [[If I had to pick something]], it would be when "
        "problems are hidden until it's too late. "
        "[[When that happens]], I talk to the person directly and privately, "
        "because usually there's a reason behind it.",
    ),
    Q(
        "relationship_problems",
        "team",
        "Have you ever had problems with someone at work?",
        "Maturidade. Ninguém se dá bem com todos; mostre como resolveu.",
        "[[Nothing serious]], but I've had misunderstandings. ((Once, a colleague and I had "
        "different expectations about a deadline)). [[We talked it through]], agreed on "
        "priorities, [[and since then]] we write down what we agree on.",
    ),
    Q(
        "disagreement",
        "team",
        "Tell me about a time you disagreed with a coworker or a manager. How did you handle it?",
        "Discordar com respeito e com dados, e depois seguir em frente.",
        "((Situation: a manager wanted to keep updating a report by hand / a colleague wanted to "
        "use a different database)). I disagreed because ((reason)). "
        "[[Instead of arguing]], I prepared a small comparison with data, "
        "[[and we decided together]]. ((Outcome)). "
        "[[Even when the decision doesn't go my way]], once it's made, I fully support it.",
        tips=("Nunca conte uma história em que o outro era incompetente.",),
    ),
    # ------------------------------------------------------- valores e pessoal
    Q(
        "free_time",
        "personal",
        "What do you like to do in your free time?",
        "Quem você é fora do trabalho. Curto e verdadeiro.",
        "[[In my free time, I like to]] ((spend time with family / exercise / travel)). "
        "[[I also enjoy]] building small side projects, like ((this app to study English with "
        "chunks, written in Python and React)).",
        tips=("Este próprio app é um ótimo exemplo de projeto pessoal: cite!",),
    ),
    Q(
        "motivates",
        "personal",
        "What motivates you?",
        "O que te faz render. Ideal se combinar com a vaga.",
        "[[What motivates me most is]] seeing people use something I built. "
        "When a report that took a day runs in seconds, or a client tells me the product changed "
        "their routine, [[that's what keeps me going]]. [[I'm also motivated by]] learning.",
    ),
    Q(
        "money_or_work",
        "personal",
        "What's more important to you: money or the work itself?",
        "Equilíbrio. Dizer só 'dinheiro' ou só 'trabalho' soa falso.",
        "[[Both matter, to be honest]]. Fair pay lets me focus on the work without worrying. "
        "[[But money alone wouldn't keep me]] in a job where I'm not learning or making an impact. "
        "[[The work itself is what keeps me engaged]].",
    ),
    Q(
        "lottery",
        "personal",
        "What would you do if you won the lottery?",
        "Pergunta descontraída: querem ver se você trabalharia mesmo sem precisar.",
        "[[First, I'd take care of my family]]. [[But I wouldn't stop working]]: I'd probably "
        "keep building software, maybe ((tools for education)), because I really enjoy it.",
    ),
    Q(
        "economy",
        "personal",
        "What's your view on the current economic situation in Brazil?",
        "Pensamento crítico sem polêmica. Evite política partidária.",
        "[[It's a challenging moment]], ((brief, neutral comment)). "
        "[[What I see in tech is that]] Brazilian developers are working more and more for "
        "international companies, [[which is a great opportunity]] for both sides: "
        "companies get talent in a close time zone, and we grow professionally.",
        tips=("Fique no neutro e volte para o trabalho remoto/internacional.",),
    ),
    Q(
        "why_hire",
        "personal",
        "Why should we hire you?",
        "Seu argumento de venda final: 3 motivos ligados à vaga.",
        "[[I'd say three reasons]]. First, I have hands-on experience with exactly what this role "
        "needs: ((Python, APIs, SQL and messy data)). Second, I've owned products end to end "
        "at PGBA, so [[I don't need someone to tell me every step]]. "
        "Third, [[I learn fast]] and I care about quality. "
        "[[I'm confident I can deliver results quickly here]].",
        tips=("Ligue cada motivo a um requisito da descrição da vaga.",),
    ),
    Q(
        "not_on_resume",
        "personal",
        "Is there anything that's not on your resume that you'd like to mention?",
        "Chance de mostrar algo extra que te diferencia.",
        "[[Actually, yes]]. I've been building ((this English-learning app)) as a side project: "
        "the same library runs in Python and in a React and TypeScript web app, with tests "
        "checking that both generate exactly the same output. "
        "[[It shows how I like to work]]: small, tested pieces that I can reuse.",
    ),
    # ----------------------------------------------------------- condições
    Q(
        "how_long",
        "conditions",
        "How long would you expect to stay with us if hired?",
        "Se você vai sair em seis meses.",
        "[[I'm looking for a long-term position]]. [[As long as]] I keep learning and "
        "contributing, I see myself here for many years.",
    ),
    Q(
        "hours_previous",
        "conditions",
        "How many hours a week did you usually work in your previous job?",
        "Ritmo de trabalho e expectativas.",
        "((Usually forty hours a week)). [[When there was a deadline or an incident]], "
        "I worked longer, but that was the exception, not the rule.",
    ),
    Q(
        "overtime",
        "conditions",
        "Are you willing to work overtime, nights or weekends?",
        "Disponibilidade. Seja honesto sobre limites.",
        "[[When it's really necessary]], like a production incident or a critical release, "
        "[[I don't see a problem with that]]. [[I just think]] it shouldn't become the routine, "
        "because good planning prevents most of it.",
    ),
    Q(
        "travel",
        "conditions",
        "Do you mind traveling on business?",
        "Disponibilidade para viagens (ex.: encontros do time remoto).",
        "[[Not at all]]. [[I'd actually enjoy]] meeting the team in person from time to time, "
        "((as long as I have some notice to organize things at home)).",
    ),
    Q(
        "relocate",
        "conditions",
        "Would you be willing to relocate?",
        "Flexibilidade. Se não puder, diga, mas sem fechar a porta de cara.",
        "((Decide before the interview.)) [[I'm open to discussing it]] if it makes sense for both "
        "sides. [[That said]], I'm fully set up to work remotely and ((I'd prefer a remote role)).",
    ),
    Q(
        "salary",
        "conditions",
        "What are your salary expectations?",
        "Se você cabe no orçamento. Evite dar um número antes de saber a faixa.",
        "[[Could you share the salary range for this position?]] "
        "((If they insist:)) Based on my research for this kind of role, "
        "[[I'm looking for something in the range of]] ((X to Y per month)). "
        "[[That said, I'm open to]] discussing the full package.",
        tips=(
            "Primeiro pergunte a faixa. Se insistirem, dê uma faixa, nunca um número só.",
            "Para vagas internacionais, pense em dólares por mês e lembre que contractor não tem "
            "13º, férias pagas nem FGTS.",
        ),
    ),
    Q(
        "start_immediately",
        "conditions",
        "Can you start immediately?",
        "Prazo real. Sair do jeito certo do emprego atual é bem visto.",
        "I'd need ((two weeks / thirty days)) to hand over my current responsibilities properly. "
        "[[I want to leave in a good way]], [[just like I'd do here]]. "
        "[[So I could start]] ((around date)).",
    ),
    # --------------------------------------------------------- suas perguntas
    Q(
        "any_questions",
        "closing",
        "Do you have any questions for us?",
        "Nunca diga 'no'. Perguntas mostram interesse e ajudam você a decidir.",
        "[[Yes, I do, thank you.]] [[What are the main challenges]] the team is facing right now?",
        tips=(
            "Leve 3 ou 4 perguntas anotadas. Use as próximas como ideias.",
            "Não pergunte de salário e benefícios na primeira conversa com o técnico.",
        ),
    ),
    Q(
        "ask_new_role",
        "closing",
        "(You ask) Is this a new position, or are you replacing someone?",
        "Entender o contexto da vaga: crescimento ou reposição.",
        "[[I was wondering]], is this a new position, [[or is it a replacement]]?",
    ),
    Q(
        "ask_report_to",
        "closing",
        "(You ask) Who would I be reporting to?",
        "Saber quem é o seu gestor e como o time se organiza.",
        "[[Who would I be reporting to]], and how is the team structured?",
    ),
    Q(
        "ask_first_months",
        "closing",
        "(You ask) What would success look like in the first three months?",
        "A melhor pergunta para vagas de tecnologia: mostra foco em resultado.",
        "[[What would success look like]] for this role in the first three months?",
    ),
    Q(
        "ask_stack",
        "closing",
        "(You ask) What does the development process look like?",
        "Como o time trabalha: deploy, revisão, testes, sprints.",
        "[[Could you tell me a bit about]] the development process? "
        "For example, how code reviews, testing and deploys work.",
    ),
    Q(
        "ask_hours",
        "closing",
        "(You ask) What are the working hours? Is overtime common?",
        "Rotina real, sobretudo em fusos diferentes.",
        "[[What are the usual working hours]] for the team, and which time zone are most people in?",
    ),
    Q(
        "ask_next_steps",
        "closing",
        "(You ask) What are the next steps in the process?",
        "Fechar a conversa sabendo o que vem depois.",
        "[[Thank you for your time.]] [[What are the next steps]] in the process?",
        tips=("Termine com uma frase positiva: 'I'm really excited about this opportunity.'",),
    ),
)

register(
    Session(
        id="tech_profile",
        title="70 perguntas frequentes (perfil tech)",
        company="Qualquer vaga de tecnologia",
        summary="As perguntas mais comuns em entrevistas em inglês, do 'tell me about yourself' "
        "ao salário, respondidas com a sua trajetória em Python, dados e produto.",
        stages=STAGES,
        questions=QUESTIONS,
    )
)
