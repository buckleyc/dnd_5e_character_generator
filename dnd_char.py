#!/usr/bin/python

# imports
from random import random, randint
import ran_gen
import die


# functions
def stat_gen():
    """Roll 4d6, drop the lowest, return total sum"""

    rolls = [die.rolld(6), die.rolld(6), die.rolld(6), die.rolld(6)]

    return sum(sorted(rolls, reverse=True)[:3])


def get_alig(alig_list):
    """
    First   [0] is lawful, neutral, chaotic
    Second  [1] is good, neutral, evil
    """

    alignment = ""
    if alig_list[0] == 1:
        alignment = alignment + "Lawful"
    elif alig_list[0] == 2:
        alignment = alignment + "Neutral"
    else:
        alignment = alignment + "Chaotic"

    if alig_list[1] == 1:
        alignment = alignment + " Good"
    elif alig_list[1] == 2:
        alignment = alignment + " Neutral"
    else:
        alignment = alignment + " Evil"

    if alig_list[0] == 2 and alig_list[1] == 2:
        alignment = "True Neutral"

    return alignment


def get_wealth_desc(w):
    """
    Return a random description of the character's appearance (GP based)
    """
    txt = ""
    if w <= 100:
        txt = open("wealth_descs/s_poor.txt", "r")

    if 100 < w <= 1250:
        txt = open("wealth_descs/poor.txt", "r")

    if 1250 < w <= 5800:
        txt = open("wealth_descs/moderate.txt", "r")

    if 5800 < w <= 12500:
        txt = open("wealth_descs/wealthy.txt", "r")

    if w > 12500:
        txt = open("wealth_descs/s_wealthy.txt", "r")

    pot_descs = txt.read().split(",   ")
    txt.close()

    return pot_descs[int(random() * (len(pot_descs) - 1))]


# body
class character:
    def __init__(self):
        # character traits
        self.p_race = ran_gen.rrace()
        self.p_class = ran_gen.rclass()
        self.p_alig_val = [die.rolld(3), die.rolld(3)]
        self.p_alignment = get_alig(self.p_alig_val)

        # attributes
        self.p_age = self.smart_age()
        self.p_fname = ran_gen.rfname(self.p_race)
        self.p_lname = ran_gen.rlname(self.p_race)
        self.p_name = self.p_fname + " " + self.p_lname

        # financial
        self.p_net_worth = ran_gen.rwealth()
        self.p_wea_desc = get_wealth_desc(self.p_net_worth)

        # stats
        self.str = stat_gen()
        self.dex = stat_gen()
        self.con = stat_gen()
        self.wis = stat_gen()
        self.int = stat_gen()
        self.cha = stat_gen()

    def logical_stereotype(self):
        """
        Helps normalize stereotypical alignment and class based
        on race according to the 5th edition PHB
        """

        # sterotypical alignment %
        ster_align = die.rolld(100)

        # stereotypical class %
        ster_class = die.rolld(100)

        if self.p_race == "Dwarf":
            if ster_align <= 98:
                self.p_alig_val[0] = 1
                self.p_alig_val[1] = 1

                if ster_class <= 48:
                    self.p_class = "Fighter"
                elif 48 < ster_class <= 96:
                    self.p_class = "Barbarian"

        elif self.p_race == "Elf":
            if ster_align <= 86:
                self.p_alig_val[0] = 3
                self.p_alig_val[1] = 1

                if ster_class <= 32:
                    self.p_class = "Ranger"
                elif 32 < ster_class <= 48:
                    self.p_class = "Sorcerer"
                elif 48 < ster_class <= 68:
                    self.p_class = "Cleric"
                elif 68 < ster_class <= 80:
                    self.p_class = "Wizard"
                elif 80 < ster_class <= 96:
                    self.p_class = "Rogue"

        elif self.p_race == "Halfling":
            if ster_align <= 97:
                self.p_alig_val[0] = 1
                self.p_alig_val[1] = 1

                if ster_class <= 25:
                    self.p_class = "Bard"
                elif 25 < ster_class <= 48:
                    self.p_class = "Rogue"
                elif 48 < ster_class <= 82:
                    self.p_class = "Cleric"
                elif 82 < ster_class <= 92:
                    self.p_class = "Monk"

        # elif self.p_race == "Human" :
        #   return get_alig(self.p_alig_val)
        #   real talk, i don't remember why this is here

        elif self.p_race == "Dragonborn":
            if ster_align <= 30:
                self.p_alig_val[0] = 1
                self.p_alig_val[1] = 1

            elif 30 < ster_align <= 60:
                self.p_alig_val[0] = 3
                self.p_alig_val[1] = 1

            elif 60 < ster_align <= 78:
                self.p_alig_val[0] = 1
                self.p_alig_val[1] = 3

            elif 78 < ster_align <= 96:
                self.p_alig_val[0] = 3
                self.p_alig_val[1] = 3

            if ster_class <= 22:
                self.p_class = "Wizard"
            elif 22 < ster_class <= 32:
                self.p_class = "Fighter"
            elif 32 < ster_class <= 48:
                self.p_class = "Sorcerer"
            elif 48 < ster_class <= 58:
                self.p_class = "Warlock"
            elif 58 < ster_class <= 72:
                self.p_class = "Paladin"
            elif 72 < ster_class <= 88:
                self.p_class = "Rogue"

        elif self.p_race == "Gnome":
            if ster_align <= 90:
                self.p_alig_val[0] = 1
                self.p_alig_val[1] = 1

            elif 90 < ster_align <= 98:
                self.p_alig_val[0] = 3
                self.p_alig_val[0] = 1

            if ster_align <= 95:
                if ster_class <= 18:
                    self.p_class = "Wizard"
                elif 18 < ster_class <= 42:
                    self.p_class = "Bard"
                elif 42 < ster_class <= 48:
                    self.p_class = "Sorcerer"
                elif 48 < ster_class <= 58:
                    self.p_class = "Warlock"
                elif 58 < ster_class <= 76:
                    self.p_class = "Paladin"
                elif 76 < ster_class <= 88:
                    self.p_class = "Sorcerer"

        elif self.p_race == "Half-Elf":  # numbers might need adjusting
            if ster_align <= 96:
                self.p_alig_val[0] = 3

                if ster_class <= 22:
                    self.p_class = "Wizard"
                elif 22 < ster_class <= 32:
                    self.p_class = "Fighter"
                elif 32 < ster_class <= 48:
                    self.p_class = "Sorcerer"
                elif 48 < ster_class <= 58:
                    self.p_class = "Warlock"
                elif 58 < ster_class <= 72:
                    self.p_class = "Paladin"
                elif 72 < ster_class <= 88:
                    self.p_class = "Rogue"

        elif self.p_race == "Half-Orc":  # numbers might need adjusting
            if ster_align <= 95:
                self.p_alig_val[0] = 3
                self.p_alig_val[1] = 2

                if ster_class <= 40:
                    self.p_class = "Barbarian"
                elif 40 < ster_class <= 80:
                    self.p_class = "Fighter"
                elif 80 < ster_class <= 90:
                    self.p_class = "Monk"
                elif 90 < ster_class <= 100:
                    self.p_class = "Paladin"

        elif self.p_race == "Tiefling":  # numbers might need adjusting
            if ster_align <= 85:
                self.p_alig_val[0] = 3
                self.p_alig_val[1] = 3

                if ster_class <= 22:
                    self.p_class = "Wizard"
                elif 22 < ster_class <= 32:
                    self.p_class = "Ranger"
                elif 32 < ster_class <= 48:
                    self.p_class = "Sorcerer"
                elif 48 < ster_class <= 58:
                    self.p_class = "Warlock"
                elif 58 < ster_class <= 72:
                    self.p_class = "Paladin"
                elif 72 < ster_class <= 88:
                    self.p_class = "Rogue"

    def smart_age(self):
        """
        Give character an appropriate age for given race
        Max age taken from 5th edition PHB, or D&D Beyond if not
        listed in PHB
        """

        # max ages
        max_dwarf_age = 433
        max_elf_age = 845
        max_halfling_age = 167
        max_human_age = 98
        max_dragonborn_age = 94
        max_gnome_age = 522
        max_halfelf_age = 222
        max_halforc_age = 80
        max_tiefling_age = 102

        # adulthood ages
        dwarf_aa = 17
        elf_aa = 17
        halfling_aa = 17
        human_aa = 17
        dragonborn_aa = 15
        gnome_aa = 20
        halfelf_aa = 17
        halforc_aa = 16
        tiefling_aa = 17

        # random percentage
        r = die.rolld(100)

        # i don't remember what tm stood for, but the intent is to help make
        # a character's age more random
        tm = randint(86, 100) / 100

        # age
        a = 1

        # this else-if block is to add variation and ensure the character
        # is of an age considered adulthood by race

        if self.p_race == "Dwarf":
            a = die.rolld(max_dwarf_age - dwarf_aa) + dwarf_aa
            if a >= int(0.74 * max_dwarf_age) and r <= 89:
                a = int(a * tm)

        elif self.p_race == "Elf":
            a = die.rolld(max_elf_age - elf_aa) + elf_aa
            if a >= int(0.88 * max_elf_age) and r <= 89:
                a = int(a * tm)

        elif self.p_race == "Halfling":
            a = die.rolld(max_halfling_age - halfling_aa) + halfling_aa
            if a >= int(0.85 * max_halfling_age) and r <= 89:
                a = int(a * tm)

        elif self.p_race == "Human":
            a = die.rolld(max_human_age - human_aa) + human_aa
            if a >= int(0.85 * max_human_age) and r <= 89:
                a = int(a * tm)

        elif self.p_race == "Dragonborn":
            a = die.rolld(max_dragonborn_age - dragonborn_aa) + dragonborn_aa
            if a >= int(0.70 * max_dragonborn_age) and r <= 85:
                a = int(a * tm)

        elif self.p_race == "Gnome":
            a = die.rolld(max_gnome_age - gnome_aa) + gnome_aa
            if a >= int(0.82 * max_gnome_age) and r <= 89:
                a = int(a * tm)

        elif self.p_race == "Half-Elf":
            a = die.rolld(max_halfelf_age - halfelf_aa) + halfelf_aa
            if a >= int(0.88 * max_halfelf_age) and r <= 89:
                a = int(a * tm)

        elif self.p_race == "Half-Orc":
            a = die.rolld(max_halforc_age - halforc_aa) + halforc_aa
            if a >= int(0.79 * max_halforc_age) and r <= 82:
                a = int(a * tm)

        elif self.p_race == "Tiefling":
            a = die.rolld(max_tiefling_age - tiefling_aa) + tiefling_aa
            if a >= int(0.82 * max_tiefling_age) and r <= 89:
                a = int(a * tm)

        # there might be some edge cases where the character's age is not adult

        return a

    def smart_wealth(self):
        """
        Make a somewhat logical attempt at calculating wealth

        This section has the most problems, probably
        """

        wealth = {
            'wretched': 10,
            'squalor': 50,
            'poor': 250,
            'modest': 1000,
            'comfortable': 4_000,
            'wealthy': 12_500,
            'aristocratic': 25_000,
        }

        p = die.rolld(1000)

        if p <= 92:
            self.p_wea_desc = 'wretched'
            self.p_net_worth = die.rolld(wealth['wretched'])
        elif 92 < p <= 500:
            self.p_wea_desc = 'poor'
            self.p_net_worth = die.rolld(wealth['poor']) + wealth['squalor']
        elif 500 < p <= 982:
            self.p_wea_desc = 'modest'
            self.p_net_worth = die.rolld(wealth['modest']) + wealth['poor']
        elif 982 < p <= 996:
            self.p_wea_desc = 'wealthy'
            self.p_net_worth = die.rolld(wealth['wealthy']) + wealth['comfortable']
        elif p > 996:
            self.p_wea_desc = 'aristocratic'
            self.p_net_worth = die.rolld(wealth['aristocratic']) + wealth['wealthy']

        # race factor
        if self.p_class == "Dwarf":
            self.p_net_worth = int(self.p_net_worth * 1.08)
        elif self.p_class == "Elf":
            self.p_net_worth = int(self.p_net_worth * 1.02)
        elif self.p_class == "Halfling":
            self.p_net_worth = int(self.p_net_worth * 1.01)
        elif self.p_class == "Human":
            self.p_net_worth = int(self.p_net_worth * 1.00)
        elif self.p_class == "Dragonborn":
            self.p_net_worth = int(self.p_net_worth * 1.02)
        elif self.p_class == "Gnome":
            self.p_net_worth = int(self.p_net_worth * 1.08)
        elif self.p_class == "Half-Elf":
            self.p_net_worth = int(self.p_net_worth * 1.02)
        elif self.p_class == "Half-Orc":
            self.p_net_worth = int(self.p_net_worth * 0.98)
        elif self.p_class == "Tiefling":
            self.p_net_worth = int(self.p_net_worth * 1.03)


    def smart_stats(self):
        "Optimizes stats based on class based on 5th edition PHB"
        ph = [self.str, self.dex, self.con, self.wis, self.int, self.cha]
        ph.sort()
        ph.reverse()
        p = die.rolld(100)

        if self.p_class == "Barbarian":
            if p <= 50:
                self.str = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.cha = ph[3]
                self.int = ph[4]
                self.wis = ph[5]
            else:
                self.str = ph[0]
                self.con = ph[1]
                self.cha = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.wis = ph[5]

        elif self.p_class == "Bard":
            self.cha = ph[0]
            self.dex = ph[1]
            self.wis = ph[2]
            self.con = ph[3]
            self.int = ph[4]
            self.str = ph[5]

        elif self.p_class == "Cleric":
            if p <= 50:
                self.wis = ph[0]
                self.str = ph[1]
                self.con = ph[2]
                self.dex = ph[3]
                self.cha = ph[4]
                self.int = ph[5]
            else:
                self.wis = ph[0]
                self.con = ph[1]
                self.str = ph[2]
                self.dex = ph[3]
                self.cha = ph[4]
                self.int = ph[5]

        elif self.p_class == "Druid":
            self.wis = ph[0]
            self.con = ph[1]
            self.dex = ph[2]
            self.cha = ph[3]
            self.int = ph[4]
            self.str = ph[5]

        elif self.p_class == "Fighter":
            if p <= 46:
                self.str = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.cha = ph[4]
                self.int = ph[5]
            elif 46 < p <= 92:
                self.dex = ph[0]
                self.con = ph[1]
                self.wis = ph[2]
                self.cha = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else:
                self.int = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.str = ph[4]
                self.cha = ph[5]

        elif self.p_class == "Monk":
            self.dex = ph[0]
            self.wis = ph[1]
            self.con = ph[2]
            self.cha = ph[3]
            self.int = ph[4]
            self.str = ph[5]

        elif self.p_class == "Paladin":
            if p <= 50:
                self.str = ph[0]
                self.cha = ph[1]
                self.wis = ph[2]
                self.dex = ph[3]
                self.con = ph[4]
                self.int = ph[5]
            else:
                self.str = ph[0]
                self.cha = ph[1]
                self.con = ph[2]
                self.dex = ph[3]
                self.wis = ph[4]
                self.int = ph[5]

        elif self.p_class == "Ranger":
            if p <= 92:
                self.dex = ph[0]
                self.wis = ph[1]
                self.con = ph[2]
                self.str = ph[3]
                self.int = ph[4]
                self.cha = ph[5]
            else:
                self.str = ph[0]
                self.wis = ph[1]
                self.con = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.cha = ph[5]

        elif self.p_class == "Rogue":
            if p <= 50:
                self.dex = ph[0]
                self.cha = ph[1]
                self.con = ph[2]
                self.wis = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else:
                self.dex = ph[0]
                self.int = ph[1]
                self.con = ph[2]
                self.wis = ph[3]
                self.cha = ph[4]
                self.str = ph[5]

        elif self.p_class == "Sorcerer":
            if p <= 50:
                self.cha = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else:
                self.cha = ph[0]
                self.con = ph[1]
                self.wis = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.str = ph[5]

        elif self.p_class == "Wizard":
            if p <= 50:
                self.int = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.str = ph[4]
                self.cha = ph[5]
            elif 50 < p <= 66:
                self.int = ph[0]
                self.dex = ph[1]
                self.con = ph[2]
                self.wis = ph[3]
                self.str = ph[4]
                self.cha = ph[5]
            else:
                self.int = ph[0]
                self.dex = ph[1]
                self.wis = ph[2]
                self.con = ph[3]
                self.str = ph[4]
                self.cha = ph[5]

        elif self.p_class == "Warlock":
            if p <= 50:
                self.cha = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else:
                self.cha = ph[0]
                self.con = ph[1]
                self.wis = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.str = ph[5]
