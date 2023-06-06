using System;

class Program
{
    static void Main()
    {
        int[] num = new int[1, 2, 3, 4, 5];

        bool vozras = true;
        bool ubivanie = true;

        for (int i = 1; i < num.Length; i++)
        {
            if (num[i] < num[i - 1])
            {
                vozras = false;
                break;
            }
        }

        for (int i = 1; i < num.Length; i++)
        {
            if (num[i] > num[i - 1])
            {
                ubivanie = false;
                break;
            }
        }

        if (vozras or ubivanie)
        {
            Console.WriteLine("Массив упорядочен");
        }
        else
        {
            Console.WriteLine("Массив не упорядочен");
        }
    }
}