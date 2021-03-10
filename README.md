# Google Hash Code 2021

## Practice Round: [Even More Pizza](practice-round/even_more_pizza.pdf)

### Problem Statement:

Given the description of the pizzas available, and the number of teams of 2, 3, or 4 people that have ordered, decide which pizzas to send to each of the teams.
The goal is to maximize, per team, the number of different ingredients used in all their pizzas.

### How we tackled the problem:

| Attempt | How to choose the teams? | How to choose the first pizza in a delivery? | How to choose the rest of the pizzas in the delivery? |
| :------ | :----------------------- | :------------------------------------------- | :---------------------------------------------------- |
| 1st | deliver to all the 4-person teams we have pizzas for, then to the 3-person teams and then to the 2-person teams | pick the one with the most ingredients | pick the one with the most ingredients |
| 2nd | deliver to all the 4-person teams we have pizzas for, then to the 3-person teams and then to the 2-person teams | pick the one with the most ingredients | pick the one with the most ingredients of the pizzas that have the least ingredients in common with the pizzas already selected for that delivery |
| 3rd | deliver to all the 4-person teams we have pizzas for, then to the 3-person teams and then to the 2-person teams | pick the one with the most ingredients | pick the one with the largest number of ingredients that weren't on any of the pizzas already selected for that delivery |

Score: 577,981,201 points

---

## Online Qualification Round: [Traffic Signaling](qualification-round/traffic-signaling.pdf)

### Problem Statement:

Given the description of a city plan and planned paths for all cars in that city, optimize the schedule of traffic lights to minimize the total amount of time spent in traffic, and help as many cars as possible reach their destination before a given deadline.

### How we tackled the problem:

| Attempt | What Libraries? | How? | What Books? | How? |
| :-------| :-------------- | :--- | :---------- | :--- |
| 1st     | x | x | x | x |

Score: 8,800,037 points

### Placements:

| Round                      | Score             | #Hub | #Country | #Worldwide |
| :------------------------- | :---------------- | :--- | :------- | :--------- |
| Online Qualification Round | 8,800,037 points | 5th | 25th | 2961th |

**#HashCodeSolved**

---

# Team πthon:

| Name               | Github                                                       | Role                                     |
| :----------------- | :----------------------------------------------------------- | :--------------------------------------- |
| Cristiano Clemente | [@cristiano-clemente](https://github.com/cristiano-clemente) | Team Leader & Programmer                 |
| Hugo Pitorro       | [@xtwigs](https://github.com/xtwigs)                         | Programmer                               |
| Catarina Carreiro  | [@cmcarreiro](https://github.com/cmcarreiro)                 | Algorithm Designer (& Bug-Finder Person) |
| Mónica Jin         | [@mokita-j](https://github.com/Mokita-J)                     | Algorithm Designer                       |

hub: [GCE-NEIIST - Instituto Superior Técnico](https://gce.rnl.tecnico.ulisboa.pt/) from [Instituto Superior Técnico](https://tecnico.ulisboa.pt/en/) (Lisbon, Portugal)
