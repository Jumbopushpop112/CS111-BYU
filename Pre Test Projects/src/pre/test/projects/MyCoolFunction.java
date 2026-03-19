/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pre.test.projects;

/**
 *
 * @author matth
 */
public class MyCoolFunction {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       int a = 5;
       int b = 0;
       int c = MyCoolFunction(a,b);
       System.out.println(MyCoolFunction(a,c));
    }
    public static int MyCoolFunction(int x, int y){
        return 2*x+y-1;
    }
    
}
