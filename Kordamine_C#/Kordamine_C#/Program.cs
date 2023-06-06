using System;
using System.Collections.Generic;

// 6. Variant

class Program
{
    static void Main()
    {
        // 1. Задано пять произвольных целых чисел (элементы массива). Определить, является ли их расположение в массиве упорядоченным (т.е. по возрастанию или по убыванию) или неупорядоченным.

        //int[] num = new int[1, 2, 3, 4, 5];

        //bool vozras = true;
        //bool ubivanie = true;

        //for (int i = 1; i < num.Length; i++)
        //{
        //    if (num[i] < num[i - 1])
        //    {
        //        vozras = false;
        //        break;
        //    }
        //}

        //for (int i = 1; i < num.Length; i++)
        //{
        //    if (num[i] > num[i - 1])
        //    {
        //        ubivanie = false;
        //        break;
        //    }
        //}

        //if (vozras or ubivanie)
        //{
        //    Console.WriteLine("Массив упорядочен");
        //}
        //else
        //{
        //    Console.WriteLine("Массив не упорядочен");
        //}

        //--------------------------------------------------------------------------

        // 2. Задан массив действительных чисел из N элементов (используйте генератор случайных чисел). Определить количество элементов, значения которых находятся вне диапазона от -10 до +10.

        //Random rand = new Random();
        //int N = 30;

        //double[] num = new double[N];

        //for (int i = 0; i < N; i++)
        //{
        //    num[i] = rand.NextDouble() * 20 - 10;
        //}

        //int vneRange = 0;

        //for (int i = 0; i < N; i++)
        //{
        //    if (num[i] < -10 || num[i] > 10)
        //    {
        //        vneRange++;
        //    }
        //}

        //Console.WriteLine($"Вне диапозона {vneRange} чисел.");

        //---------------------------------------------------------------------------

        //3. Дано: информация о каждом жителе города содержит следующие элементы:
        //а) фамилия, имя, отчество;
        //б) домашний адрес(улица, дом);
        //в) дата рождения.
        //Информация о жителе является элементом одного большого массива М[ ].
        //Требуется составить списки избирателей, живущих по заданному адресу в алфавитном порядке.
        //Примечание: Правом участия в выборах обладают люди не моложе 18 лет.

        //    class zhitel
        //{
        //    public string perenimi { get; set; }
        //    public string name { get; set; }
        //    public string otchestvo { get; set; }
        //    public string ulica { get; set; }
        //    public string dom { get; set; }
        //    public DateTime data { get; set; }
        //}
        //    zhitel[] zhiteli = new zhitel[]
        //    {
        //        new zhitel { perenimi = "Chinikov", name = "Nikita", otchestvo = "Ivanov", ulica = "Sopruse tee", dom = "24", data = new DateTime(1990, 5, 12) },
        //        new zhitel { perenimi = "Jones", name = "Ivan", otchestvo = "Viktorovich", ulica = "Sopruse tee", dom = "24", data = new DateTime(1985, 9, 20) },
        //        new zhitel { perenimi = "Murat", name = "Migel", otchestvo = "Ronovich", ulica = "Sopruse tee", dom = "24", data = new DateTime(2000, 2, 8) },
        //        new zhitel { perenimi = "Nikulina", name = "Nastja", otchestvo = "Porfirevich", ulica = "Sopruse tee", dom = "24", data = new DateTime(1978, 12, 15) },
        //    };


        //    List<zhitel> golos = new List<zhitel>();

        //    foreach (zhitel i in zhiteli)
        //    {
        //        if (i.ulica == "Sopruse tee" && i.dom == "24" && notwoman(i.DateOfBirth))
        //        {
        //            golos.Add(i);
        //        }
        //    }

        //    golos.Sort((x, y) => x.perenimi.CompareTo(y.perenimi));

        //    Console.WriteLine("Golosocacshih na Sopruse tee 24");
        //    foreach (Zhitel i in golos)
        //    {
        //        Console.WriteLine("{0}, {1} {2}", i.perenimi, i.name, i.otchestvo);
        //    }

        //    static bool notwoman(DateTime dateOfBirth)
        //    {
        //        int age = DateTime.Today.Year - dateOfBirth.Year;
        //        if (dateOfBirth > DateTime.Today.AddYears(-age))
        //        {
        //            age--;
        //        }

        //        return age >= 18;
        //    }

        //}
    }