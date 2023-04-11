using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project_c_sharp
{
    public class Alamprog
    {
        public static int Korruta(int arv1, int arv2)
        {
            return arv1 * arv2;
        }

        public static void Tere(string name)
        {
            Console.WriteLine("Tere {0}", name);
        }

        public static int Keskmine(int n, int arv1, int arv2)
        {
            return (arv1 + arv2) / n;
        }

        public static double Jagata(int arv1, int arv2)
        {
            double j = arv1 / arv2;
            j = Math.Round(j, 2);
            return j;
        }

        public static string Klakulaator(int arv1, int arv2, char tehe)
        {
            System.Data.DataTable table = new System.Data.DataTable();
            double j = Convert.ToDouble(table.Compute(arv1.ToString() + tehe.ToString() + arv2.ToString(), String.Empty));
            j = Math.Round(j, 0);
            string vastus = "";
            string nurr = "nurr ";
            for (int i = 0; i < Math.Abs(Convert.ToInt32(j)); i++)
            {
                vastus = vastus + nurr;
            }
            return vastus;
        }
        public static string Stars(int n)
        {
            string var = "";
            for (int i = 0; i < n; i++)
            {
                var += "*";
            }
            return var;
        }
        public static void NStars(int j)
        {
            int[] stars = new int[j];
            for (int i = 0; i < j; i++)
            {
                Console.WriteLine("{0} arv", i + 1);
                stars[i] = Convert.ToInt32(Console.ReadLine());
            }
            foreach (int num in stars)
            {
                Console.Write(Stars(num));
                Console.WriteLine();
            }
        }
    }
}
