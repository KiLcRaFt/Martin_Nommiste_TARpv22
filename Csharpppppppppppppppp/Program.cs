using System;
using System.Collections.Generic;

// 6. Variant

//class Program
//{

    //static void Main(string[] args)
    //{
        // 1. Задано пять произвольных целых чисел (элементы массива). Определить, является ли их расположение в массиве упорядоченным (т.е. по возрастанию или по убыванию) или неупорядоченным.

        //int[] num = new int[5] {5,4,3,2,1};

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

        //if (vozras || ubivanie)
        //{
        //    Console.WriteLine("Массив упорядочен");
        //}
        //else
        //{
        //    Console.WriteLine("Массив не упорядочен");
        //}

        //--------------------------------------------------------------------------

        // 2. Задан массив действительных чисел из N элементов (используйте генератор случайных чисел). Определить количество элементов, значения которых находятся вне диапазона от -10 до +10.

        //var N = 30;
        //var a = new int[N];
        //var rand = new Random();
        //var count = 0;
        //for (var i = 0; i < N; i++)
        //{
        //    a[i] = rand.Next(-15, 15);
        //    if (a[i] < -10) count++;
        //    else if (a[i] > 10) count++;
        //}
        //Console.WriteLine("Vne diapazona " + count + " chisel");

        //---------------------------------------------------------------------------

        //3. Дано: информация о каждом жителе города содержит следующие элементы:
        //а) фамилия, имя, отчество;
        //б) домашний адрес(улица, дом);
        //в) дата рождения.
        //Информация о жителе является элементом одного большого массива М[ ].
        //Требуется составить списки избирателей, живущих по заданному адресу в алфавитном порядке.
        //Примечание: Правом участия в выборах обладают люди не моложе 18 лет.


        //zhitel[] M = new zhitel[]
        //{
        //                    new zhitel { perenimi = "Chinikov", name = "Nikita", otchestvo = "Ivanov", ulica = "Sopruse tee", dom = "24", data = new DateTime(1990, 5, 12) },
        //                    new zhitel { perenimi = "Jones", name = "Ivan", otchestvo = "Viktorovich", ulica = "Sopruse tee", dom = "24", data = new DateTime(2007, 9, 20) },
        //                    new zhitel { perenimi = "Murat", name = "Migel", otchestvo = "Ronovich", ulica = "majaka tee", dom = "25", data = new DateTime(2000, 2, 8) },
        //                    new zhitel { perenimi = "Nikulina", name = "Nastja", otchestvo = "Porfirevich", ulica = "Sopruse tee", dom = "24", data = new DateTime(1978, 12, 15) },
        //};

        //List<zhitel> golos = new List<zhitel>();
            
        //foreach (zhitel i in M)
        //{
        //        if (i.ulica == "Sopruse tee" && i.dom == "24" && nemaloi(i.data))
        //        {
        //            golos.Add(i);
        //        }
        //}

        //golos.Sort((x, y) => x.perenimi.CompareTo(y.perenimi));

        //Console.WriteLine("Голосование на Sopruse tee 24");
        //Console.WriteLine("");
        //foreach (zhitel i in golos)
        //{
        //    Console.WriteLine("Фамилия:{0}", i.perenimi);
        //    Console.WriteLine("Имя:{0}", i.name);
        //    Console.WriteLine("Отчество:{0}", i.otchestvo);
        //    Console.WriteLine("");
        //}

        //static bool nemaloi(DateTime dateOfBirth)
        //{
        //    int age = DateTime.Today.Year - dateOfBirth.Year;
        //    if (dateOfBirth > DateTime.Today.AddYears(-age))
        //    {
        //        age--;
        //    }

        //    return age > 18;
        //}    
    //}
    //class zhitel
    //{
    //    public string perenimi { get; set; }
    //    public string name { get; set; }
    //    public string otchestvo { get; set; }
    //    public string ulica { get; set; }
    //    public string dom { get; set; }
    //    public DateTime data { get; set; }
    //}
//}