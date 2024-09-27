import random

hp = int(100)
pahan_respect = int(0)
security_respect = int(0)
srok = int(30)

#Это переменные для сравнения параметра уважения охраны
security_respect_0 = -10
security_respect_1 = -5
security_respect_2 = 10
security_respect_3 = 20



#Это переменные для сравнения параметра уважения Пахана
pahan_respect_0 = -10
pahan_respect_1 = -5
pahan_respect_2 = 10
pahan_respect_3 = 20

appelation_count = 0


def status(): #функция вывода текущих показателей здоровья, репутации, и остатка срока
    if pahan_respect <= pahan_respect_0:
        pahan_respect_text = 'Отвратительная'
    if pahan_respect_0 < pahan_respect <= pahan_respect_1:
        pahan_respect_text = 'Плохая'
    if pahan_respect_1 < pahan_respect <= pahan_respect_2:
        pahan_respect_text = 'Нормальная'
    if pahan_respect_2 < pahan_respect <= pahan_respect_3:
        pahan_respect_text = 'Хорошая'
    if pahan_respect > pahan_respect_3:
        pahan_respect_text = 'Отличная'

    if security_respect <= security_respect_0:
        security_respect_text = 'Отвратительная'
    if security_respect_0 < security_respect <= security_respect_1:
        security_respect_text = 'Плохая'
    if security_respect_1 < security_respect <= security_respect_2:
        security_respect_text = 'Нормальная'
    if security_respect_2 < security_respect <= security_respect_3:
        security_respect_text = 'Хорошая'
    if security_respect > security_respect_3:
        security_respect_text = 'Отличная'

    print()
    print(f'Ваше текущее здоровье: {hp}')
    print(f'Ваша репутация с Паханом: {pahan_respect_text}')
    print(f'Ваша репутация с охраной: {security_respect_text}')
    print(f'Вам осталось сидеть: {srok} недель')
    print()

def trial(): #функция первоначального "экрана" суда, где можно либо признаться, либо отрицать обвинения
    status()
    trial_end = False
    global srok, hp
    print('Вас несправдливо обвинили в том, что вы нанесли тяжкий вред сотруднику полиции,хотя вы всего лишь кинули в него стаканчик.')
    print('Судья внимательно смотрит на вас, и спрашивает:')
    print('"Признаёте ли вы себя виновным в данном тяжком преступлении?"')
    while trial_end == False:
        print('1. Признаться')
        print('2. Отвергнуть обвинения')
        answer = input('> ')
        if answer == '1':
            print('Вы говорите: "Да, всё верно, я признаюсь в этой ужасном преступлении')
            srok = srok - 10
            print(f'Судья говорит: "Приговариваю вас к {srok} неделям заключения в тюрьме "Каменная лужа"!')
            hp -= 10
            print('Вам невообразимо тяжко на душе, так как вы признаётесь в том, чего не совершали.')
            print()
            trial_end = True
        elif answer == '2':
            print('Вы говорите: "Я отрицаю ваши обвинения, этот суд фальшивка и не имеет ничего общего со справедливостью!"')
            srok = srok + 10
            print(f'Судья говорит: "За ваше отрицание справедливости данного суда приговарию Вас к {srok} неделям заключения в тюрьме "Каменная лужа"!')
            trial_end = True
        else:
            print('Пожалуйста, выберите вариант ответа')

def prison_entry(): #функция сцены первого захода в камеру
    status()
    prison_entry_end = False
    global pahan_respect, security_respect, hp
    print('''
Спустя несколько часов вас привозят в тюрьму "Каменная лужа". Сопровождающий вас надзиратель провожает вас до вашей камеры, упёршись чем-то твёрдым в вас сзади.
"Ну что, подоночек, добро пожаловать домой!" - неприятно крикнул офицер, смачно плюнув на Вашу куртку.
Взглянув внутрь камеры, вы обнаруживаете нескольких сидящих заключенных, причём один из них явно имеет более важный вид, чем остальные.
Видимо, это и есть Пахан.
У Вас есть возможность проявить себя и уважить заключенного-ветерана, а можете тихо-мирно проследовать в камеру''')
    print('Как будете поступать?')
    while prison_entry_end == False:
        print('')
        print('1. Тихо-мирно проследовать в камеру')
        print('2. Крикнуть "Вечер в хату!"')
        print('3. Попытаться утянуть за собой сопровождающего')
        answer = input('> ')
        if answer == '1':
            print('Пока вы тихо-мирно проходите к своей шконке, Пахан разочарованно говорит "Пф, ещё один петушара походу прибыл, не знает, как правильно входить"')
            print('Сопровождающий ухмыляется: "Ну хоть с этим проблем не будет"')
            pahan_respect = pahan_respect - 2
            security_respect = security_respect + 2
            prison_entry_end = True
        elif answer == '2':
            print('Вы громко кричите "ВЕЧЕР В ХАТУ". Услышав это, Пахан довольно улыбается: "Ооо, сразу видно, бывалый малый!"')
            print('Сопровождающий разочарованно вздыхает')
            pahan_respect += 2
            security_respect -=2
            prison_entry_end = True
        elif answer == '3':
            print('Вы пытаетесь утянуть за собой офицера, но вместо удачной попытки получаете дубинкой по голове.')
            print('Несмотря на злого сопровождающего и адскую боль в виске, мы слышите злачное одобрение Пахана: "ХВАТАЙТЕ ЕГО РЕБЯТА"')
            print('Надзирающий успевает скрыться за дверью прежде, чем заключенные успели что-либо сделать')
            pahan_respect +=4
            security_respect -=4
            hp -= 30
            prison_entry_end = True
        else:
            print('Пожалуйста, введите вариант ответа')
    print('Сразу после этого дверь резко закрывается, и Вы остаётесь наедине со своими новыми соседями')



def daily_prison(): #основной экран выбора мероприятий
    global pahan_respect, security_respect, hp, srok
    daily_prison_end = False
    if hp >= 100:
        hp = 100
    status()
    if srok <= 0: #если срок пришёл к концу - то победа
        victory()
    if hp <= 0:
        death('К сожалению, вы не смогли принять правила и выжить в тюрьме "Каменная лужа"')
    while daily_prison_end == False:
        print('')
        print('Вот и настал новый день в вашей родной камере')
        print('Чем будете заниматься?')
        print('')
        print('1. Ничем, лучше отдохну')
        print('2. Пойду поработаю')
        print('3. Стучать на сокамерников')
        print('4. Стоять на стрёме')
        print('5. Донимать охранников по просьбе Пахана')

        if pahan_respect > pahan_respect_2:
            print('6. Попытаться сбежать')
        if security_respect > security_respect_2:
            print('7. Попросить Апелляцию')
        answer = input('> ')
        if answer == '1':
            rest1()
            daily_prison_end = True
        elif answer == '2':
            work2()
            daily_prison_end = True
        elif answer == '3':
            stuchat3()
            daily_prison_end = True
        elif answer == '4':
            strem4()
            daily_prison_end = True
        elif answer == '5':
            annoy5()
            daily_prison_end = True
        elif answer == '6' and pahan_respect > pahan_respect_2:
            escape6()
            daily_prison_end = True
        elif answer == '7' and security_respect > security_respect_2:
            appelation7()
            daily_prison_end = True
        else:
            print('Пожалуйста, введите вариант ответа')
    




def rest1(): #экран1, отдых
    global hp
    print ('Вы решаете сегодня ничего не делать и просто полежать на кровати')
    print ('Вы восстановили немного здоровья')
    hp +=10


def work2(): #Экран2, работа
    status()
    global pahan_respect, security_respect
    print('Сегодня вы решили поработать на благо родной тюрьмы. Вы пошли шить вместе с солевыми наркоманами футболки')
    print('Ваша репутация с охраной увеличилась, а с сокамерниками уменьшилась')
    pahan_respect -= 2
    security_respect +=2


def stuchat3(): #Экран3, стучать
    global hp, pahan_respect, security_respect, pahan_respect_1, pahan_respect_0
    print('Сегодня вы решили стучать на своих соседей. Им это явно не понравится')
    pahan_respect -=4
    security_respect +=4
    if pahan_respect_0 < pahan_respect <= pahan_respect_1:
        print('Ваши сокамерники узнали о вашей нехорошей затее и решили хорошенько вас наказать')
        hp -= 10
    elif pahan_respect < pahan_respect_0:
        print('Ваши выходки надоели Пахану и он приказал избить вас до полусмерти')
        hp -=30


def strem4(): #Экран4, Стоять на стрёме
    global pahan_respect, security_respect
    print('Сегодня вы решили постоять на стрёме, чтобы соседям было комфортно отдыхать и заниматься своими делами')
    print('Охрана просто так это не оставит')
    pahan_respect +=2
    security_respect -=2

def annoy5(): #Экран5, донимать охранников
    global hp, pahan_respect, security_respect, security_respect_1, security_respect_0
    print('Сегодня по просьбе Пахана вы решили донимать охранников')
    pahan_respect +=4
    security_respect -=4
    if security_respect_2 < security_respect < security_respect_1: 
        print('Вашим надзирателям надоело слушать ваши истошные крики, и они решили вас наказать')
        hp -=10
    elif security_respect < security_respect_0 : 
        print('Вы настолько надоели охранникам, что они решили испытать на вас новый тазер-пистолет')
        hp -=30

def escape6(): #Экран6, побег
    global hp, pahan_respect, security_respect, pahan_respect_2, pahan_respect_3, srok
    print('Пахан по секрету вам рассказывает о том, что есть небольшая щель в стене тюрьмы, через которую можно пробраться наружу.')
    print('Вы решаетесь попробовать пробраться через неё')
    if pahan_respect < pahan_respect_3:
        print('Пахан сказал, что помогать вам не будет и вам придётся всё делать самому')
        print('К сожалению, в одиночку вы в определенный момент застреваете в стене, и лишь удар дубинкой по вашей заднице пробуждает в вас понимание того, что побег вышел неудачным')
        print('За вашу выходку вам накинули ещё 5 недель')
        srok += 5
        hp -= 20
    elif pahan_respect >= pahan_respect_3:
        print('Пахан сказал, что вы у него на хорошем слуху, и он готов помочь вам в осуществлении побега')
        print('Отправив с вами пару человек, вы толпой отправились к тюремной стене. Исследовав её на предмет прохода, вы находите небольшую щель, в которую можно еле протиснуться.')
        print('Вы пытаетесь влезть в щель, и понимаете, что застряли. Подав голос, сопровождающие толкают вас наружу, и вы с трудом выкарабкиваетесь наружу.')
        print('Ура! Долгожданная свобода!')
        victory()

def appelation7(): #экран7, аппеляция
    global hp, pahan_respect, security_respect, security_respect_2, security_respect_3, srok, appelation_count
    print('Зная, что вы на хорошем слуху у начальства, вы решаетесь подать аппеляцию по выходу на УДО.')
    if security_respect_2 < security_respect < security_respect_3 and appelation_count != 1:
        print('На аппеляции вас хвалят за добросовестную работу, поэтому в качестве благодарности ваш срок уменьшают вдвое')
        srok = srok // 2
        print('К сожалению, когда вы возвращаетесь в камеру, Пахану сильно не нравится то, что вы лобызаетесь с начальством тюрьмы. За это вас прилично бьют')
        hp -=20
        appelation_count = 1
    elif security_respect < security_respect_3 and appelation_count == 1:
        print('К сожалению, вы уже просили об апелляции, а с надзирателями вы не успели достаточно сдружиться, чтобы вас порекомендовать комменданту к выпуску по УДО')
        print('Сокамерники узнали о ваших планах об очередной апелляции, и показали, что бывает с теми, кому тут не нравится')
        hp -= 10
    elif security_respect >= security_respect_3:
        print('Ваши достижения на пути исправления очень сильно впечатляют коменданта. Ваша апелляция удовлетворена, и вы, наконец, можете отсюда выйти')
        print('Ура! Долгожданная свобода!')
        victory()
        


        
    


def random_event_0(): #Случайный эвент 0 - оголённый провод
    global hp
    random_event_end = False
    print('Вы случайно натыкаетесь на оголённый провод: судя по искрам, он под напряжением.')
    print('Что вы будете делать?')
    print('1. Обойти маленькими шажками искрящийся провод')
    print('2. Как можно большими шагами обойти искрящийся провод')
    print('3. Подойти к проводу и положить оголённый конец себе в рот, надеясь получить сверх-способности')
    while random_event_end == False:
        answer = input('> ')
        if answer == '1':
            print('Вспомнив про шаговое напряжение, вы малюсенькими шажками, чтобы разность потенциалов не пробивала вашу кожу, обходите искрящийся провод')
            random_event_end = True
        elif answer == '2':
            print('Надеясь увернуться от искрящегося провода, вы огромными шагами пытаетесь пройти по полу. Но разность напряжений бьёт по вам ударом тока, вы чувствуете неприятный электрический удар.')
            hp -=15
            random_event_end = True
        elif answer == '3':
            print('Слушая голоса в своей голове, вы берёте провод сначала в свои руки, а после кладёте оголённый провод себе в рот, надеясь получить таким образом сверх-способности. К сожалению, электрический ток работает не так, и 220 вольт проходят через ваш мозг.')
            death('220 вольт оказались несовместимы с вашей жизнью')
        else:
            print('Пожалуйста, введите вариант ответа')

def random_event_1(): #Случайный эвент 1 - медсестра
    global hp, pahan_respect, security_respect
    random_event_end = False
    print('Пока вы играли в карты с сокамерниками мимо вашей камеры проходила симпатичная медсестра в сопровождении охранника. Увидев ваше скорбное лицо, она предложила пройти с ней в медкабинет.')
    print('1. Соглашаетесь.')
    print('2. Отказываетесь.')
    while random_event_end == False:
        answer = input('> ')
        if answer == '1':
            print('Вы соглашаетесь пройти вместе с медсестрой в лазарет. Ваши сопартийцы недовольны тем, что вы бросили партию в карты.')
            pahan_respect -=3
            random_event_end = True
            print('Вы проходите с медсестрой и охранником в медкабинет. Ведя какие-то записи, у вас спрашивают:')
            print('Жалобы есть?')
            random_event_end1 = False
            while random_event_end1 == False:
                print('1. Да, меня всего побили вчера. Очень болит всё.')
                print('2. Да, в моем организме острая недостача женского тепла.')
                print('3. Да знаете, всё в порядке! Просто всегда приятно выбраться из той жуткой камеры')
                answer1 = input('> ')
                if answer1 == '1':
                    print('Ничего страшного, щас укольчик поставим, сразу встанете на ноги')
                    print('Вам ставят укол, и вы чувствуете, что вам становится лучше')
                    hp += 35
                    random_event_end1 = True
                elif answer1 == '2':
                    print('Вы чувствуете, как сзади по голове вас огрели чем-то тяжелым. А после этого почувствовали яркий всплеск эмоций в своём паху')
                    hp -=35
                    random_event_end1 = True
                elif answer1 == '3':
                    print('Медсестра понимающе кивает, и даёт вам просто посидеть в тишине в течение получаса')
                    security_respect +=3
                    hp +=15
                    random_event_end1 = True
                else:
                    print('Пожалуйста, введите вариант ответа')
                    
        if answer == '2':
            print('Вы говорите, что вам и тут неплохо и никуда не уходите, партию всё таки надо доиграть.')
            pahan_respect += 3
            random_event_end = True
        else:
            print('Пожалуйста, введите вариант ответа')
                  

def random_event_2(): # Рандомный эвент 2 - драка с петухом
    global hp, pahan_respect, security_respect
    random_event_end = False
    print('Во время прогулки вы увидели, как один из подчиненных Пахана пытается драться с охранником. Что будете делать?')
    print('1. Разнять их')
    print('2. Помочь подчиненному Пахана')
    print('3. Помочь охраннику отпинать подчиненного Пахана')
    print('4. Пройти мимо')
    while random_event_end == False:
        answer = input('> ')
        if answer == '1':
            print('Вы пытаетесь разнять дерущихся, но в итоге получаете люлей от обоих')
            hp -= 15
            random_event_end = True
        elif answer == '2':
            print('Вы помогаете отбиться от охранника, но потом узнаете человека, которому решили помочь: это один из местных "петухов". За такое вас в камере не погладят.')
            print('Охранник же запомнил вас и вашу выходку')
            pahan_respect -= 3
            security_respect -= 3
            random_event_end = True
        elif answer == '3':
            print('Вы помогаете охраннику отбиться от зэка, и взглянув на его поближе, узнаёте, что это один из местных "петушков". Надо будет рассказать Пахану о своём подвиге!')
            print('Охранник же поблагодарил вас за помощь')
            pahan_respect += 3
            security_respect +=3
            random_event_end = True
        elif answer == '4':
            print('Вы просто проходите мимо, не желая ни в чём участвовать')
            random_event_end = True
        else:
            print('Пожалуйста, введите вариант ответа')
    
def random_event_3(): # Рандомный эвент 3 - драка с Бывалым (возможно можно рандом эвент 2 и 3 объединить, но мне впадлу пока)
    global hp, pahan_respect, security_respect
    random_event_end = False
    print('Во время прогулки вы увидели, как один из подчиненных Пахана пытается драться с охранником. Что будете делать?')
    print('1. Разнять их')
    print('2. Помочь подчиненному Пахана')
    print('3. Помочь охраннику отпинать подчиненного Пахана')
    print('4. Пройти мимо')
    while random_event_end == False:
        answer = input('> ')
        if answer == '1':
            print('Вы пытаетесь разнять дерущихся, но в итоге получаете люлей от обоих')
            hp -= 15
            random_event_end = True
        elif answer == '2':
            print('Вы помогаете отбиться от охранника, но потом узнаете человека, которому решили помочь: это один из местных "Бывалых". Пахан скажет спасибо, что помогли его близкому подчиненному!.')
            print('Охранник же запомнил вас и вашу выходку')
            pahan_respect += 3
            security_respect -= 3
            random_event_end = True
        elif answer == '3':
            print('Вы помогаете охраннику отбиться от зэка, и взглянув на его поближе, узнаёте, что это один из "Бывалых" Пахана. Вы чувствуете, что в камере вам будут не рады!')
            print('Охранник же поблагодарил вас за помощь')
            pahan_respect -= 5
            security_respect +=3
            random_event_end = True
        elif answer == '4':
            print('Вы просто проходите мимо, не желая ни в чём участвовать')
            random_event_end = True
        else:
            print('Пожалуйста, введите вариант ответа')

def random_event(event): #попытка имплеминтировать рандомные события
    if event == 0: 
        random_event_0() #Рандомный эвент 0 - оголённый провод
    elif event == 1: 
        random_event_1() #Рандомный эвент 1 - поход к медсестре
    elif event ==2:
        random_event_2() #Рандомный эвент 2 - Драка с Петушком
    elif event == 3:
        random_event_3() #Рандомный эвент 2 - Драка с Бывалым

#randev = random.randint(0,3)
#random_event(randev)



def death(why_dead): #экран смерти
    global hp
    print(why_dead)
    exit(0)

def victory(): #Экран победы
    print('Наконец-то вы выбрались из этой ужасной тюрьмы. Но стали ли вы более законопослушным? Или тюрьма окончательно вас сломала и направила по кривой дорожке? Лишь время покажет')
    exit(0)

trial() #Начало игры, суд

prison_entry() #Первоначальный вход в тюрягу

while srok >= 0: #основной цикл на повторение ежедневного выбора мероприятий
    daily_prison() #запуск основного выбора мероприятия
    srok -= 1 
    randtest = random.randint(0,4) #проверка на прок рандомного эвента
    if randtest == 1:
        randev = random.randint(0,3) #выбор аргумента для рандомного эвента
        random_event(randev) #запуск рандомного эвента

        


