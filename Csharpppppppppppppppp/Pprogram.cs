using System;
using System.Collections.Generic;

// 6. Variant

class Pprogram
{

    static void Main(string[] args)
    {
        // 1. Küsi kasutajalt viis arvu, salvesta neid massiivi ning väljasta nende summa, aritmeetiline keskmine ja korrutis.

        //int[] numbers = new int[5];

        //for (int i = 0; i < numbers.Length; i++)
        //{
        //    Console.Write("Chislo {0}: ", i + 1);
        //    numbers[i] = Convert.ToInt32(Console.ReadLine());
        //}

        //int sum = 0;
        //for (int i = 0; i < numbers.Length; i++)
        //{
        //    sum += numbers[i];
        //}

        //double srednie = (double)sum / numbers.Length;

        //int umnozhenie = 1;
        //for (int i = 0; i < numbers.Length; i++)
        //{
        //    umnozhenie *= numbers[i];
        //}

        //Console.WriteLine("Summa: {0}", sum);
        //Console.WriteLine("Srednie: {0}", srednie);
        //Console.WriteLine("Peremnozhenie: {0}", umnozhenie);

        // -------------------------------------------------------------------------------------------------------------

        // 2. Ütle kasutajale "Osta elevant ära!". Senikaua korda küsimust, kuni kasutaja lõpuks ise kirjutab "elevant".

        //string user = "";

        //while (user.ToLower() != "slon")
        //{
        //    Console.Write("Kupi slona! ");
        //    user = Console.ReadLine();
        //}

        //Console.WriteLine("Pasjambus <3");

        // -------------------------------------------------------------------------------------------------------------

        //3.Koosta alamprogramm etteantud arvu tärnide väljatrükiks. 

        //  Console.Write("Skolko * : ");
        //  int kol = Convert.ToInt32(Console.ReadLine());

        //  Star(kol);

        //  Console.ReadKey();

        // -------------------------------------------------------------------------------------------------------------

        //4.Küsi inimeselt kolm arvu. Iga arvu puhul joonista vastav kogus tärne ekraanile.

        //int[] num = new int[3];

        //for (int i = 0; i < 3; i++)
        //{
        //    Console.Write("Chislo {0}: ", i + 1);
        //    num[i] = Convert.ToInt32(Console.ReadLine());
        //}

        //Console.WriteLine();

        //for (int i = 0; i < 3; i++)
        //{
        //    Star(num[i]);
        //    Console.WriteLine();
        //}

        // -------------------------------------------------------------------------------------------------------------

        //5.Дан список из 20 случайных чисел. Переписать его элементы в новый список следующим образом: сначала все четные, затем все нечетные.

        //List<int> numbers = random(20);
        //List<int> nums = new List<int>();
        //List<int> chotnoe = new List<int>();
        //List<int> nechotnoe = new List<int>();

        //foreach (int number in numbers)
        //{
        //    if (number % 2 == 0)
        //    {
        //        chotnoe.Add(number);
        //    }
        //    else
        //    {
        //        nechotnoe.Add(number);
        //    }
        //}

        //nums.AddRange(chotnoe);
        //nums.AddRange(nechotnoe);

        //foreach (int number in nums)
        //{
        //    Console.Write(number + " ");
        //}

        // -------------------------------------------------------------------------------------------------------------

        //6. Нaпишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его cоседей. Для элeментов списка, являющиxся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся cписок «1 3 5 6 10», то на выход ожидается cписок «13 6 9 15 7».
        //Если на вход пришло только однo число, надо вывести его же.
        //Вывoд должен содержать одну строку с чиcлами новoго списка, разделёнными пробeлом.

        //Console.WriteLine("Chisla s probelom: ");
        //string input = Console.ReadLine();

        //List<int> numbers = input.Split(' ').Select(int.Parse).ToList();

        //List<int> result = sum(numbers);

        //Console.WriteLine(string.Join(" ", result));
    }

    //3.4.
    //static void Star(int a)
    //{
    //    for (int i = 0; i < a; i++)
    //    {
    //        Console.Write("*");
    //    }
    //} 

    // -------------------------------------------------------------------------------------------------------------

    // 5.
    //static List<int> random(int a)
    //{
    //    List<int> numbers = new List<int>();
    //    Random random = new Random();

    //    for (int i = 0; i < a; i++)
    //    {
    //        numbers.Add(random.Next(1, 100));
    //    }

    //    return numbers;
    //}

    // -------------------------------------------------------------------------------------------------------------

    //6.
    //static List<int> sum(List<int> numbers)
    //{
    //    List<int> result = new List<int>();

    //    int num = numbers.Count;

    //    if (num == 1)
    //    {
    //        return numbers;
    //    }

    //    for (int i = 0; i < num; i++)
    //    {
    //        int firstnum = (i - 1 + num) % num;
    //        int secnum = (i + 1) % num;

    //        int sum = numbers[firstnum] + numbers[secnum];
    //        result.Add(sum);
    //    }

    //    return result;
    //}
}

