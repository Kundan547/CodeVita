import java.util.Scanner;

public class WeirdFaculty {

    public static int findWeirdFacultyIndex(int[] scores) {
        int totalSum = 0;
        // Calculate total sum of scores (this will help us calculate right side sum)
        for (int score : scores) {
            totalSum += score;
        }

        int leftSum = 0;

        // Traverse through the array and keep track of left sum and right sum
        for (int i = 0; i < scores.length; i++) {
            totalSum -= scores[i];  // Now totalSum is the right side sum
            
            if (leftSum > totalSum) {
                return i;  // This is the point where left sum is greater than right sum
            }
            
            leftSum += scores[i];  // Update left sum for the next iteration
        }

        // If no such index is found
        return -1;
    }

    public static void main(String[] args) {
        // Example input
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of scores:");
        int n = sc.nextInt();
        int[] scores = new int[n];
        
        System.out.println("Enter the scores:");
        for (int i = 0; i < n; i++) {
            scores[i] = sc.nextInt();
        }
        
        int result = findWeirdFacultyIndex(scores);
        
        if (result != -1) {
            System.out.println("The weird faculty index is: " + result);
        } else {
            System.out.println("No such index found.");
        }
        
        sc.close();
    }
}
