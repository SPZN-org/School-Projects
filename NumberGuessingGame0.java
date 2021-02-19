import java.util.Scanner;
import java.util.Random;
public class NumberGuessingGame0 {
	private static Random r = new Random();
	private static Scanner in = new Scanner(System.in);
	private static int generatedRandomNumber;
	private static int numberOfGuesses;


	
	public static void main(String[] args) {
		playNumberGuessingGame();
		
	}
	
	public static void playNumberGuessingGame() {
		generatedRandomNumber = r.nextInt(5001);
		askUserToGuessRandomNumber();
		numberOfGuesses = 0;
		loopUntilPlayerGuessIsCorrect();	
	}
	
	private static void loopUntilPlayerGuessIsCorrect() {
		
		boolean playerGuessIsWrong = true;
		
		while(playerGuessIsWrong) {
			int numberGuessedByUser = readAndReturnUserGuessAtRandomNumber();
			numberOfGuesses++;
			String feedbackMessage = getAndReturnFeedbackMessageForUser(numberGuessedByUser);
		    showFeedbackMessageToUser(feedbackMessage);
		    playerGuessIsWrong = numberGuessedByUserEqualsNotToGeneratedRandomNumber(numberGuessedByUser);
		}
	}
	
	private static void askUserToGuessRandomNumber() {
		System.out.println("Please enter any number from 0 to 5000: ");
	}
	
	private static int readAndReturnUserGuessAtRandomNumber() {
		return Integer.parseInt(in.nextLine());
	}
	
	private static String getAndReturnFeedbackMessageForUser(int numberGuessedByUser) {
		
		String feedbackMessageForUser="";
		
		if (numberGuessedByUserEqualsToGeneratedRandomNumber(numberGuessedByUser)) {
			feedbackMessageForUser = getFeedbackMessageForUserGuessIsCorrect();
		} else if (numberGuessedByUserIsMoreThanGeneratedRandomNumber(numberGuessedByUser)) {//change to method
			feedbackMessageForUser = getFeedbackMessageForNumberGuessedByUserTooHigh();
		} else if (numberGuessedByUserIsLessThanGeneratedRandomNumber(numberGuessedByUser)) { //change to method
			feedbackMessageForUser = getFeedbackMessageForNumberGuessedByUserTooLow();
		} 
		
		return feedbackMessageForUser;

	}

	private static boolean numberGuessedByUserEqualsNotToGeneratedRandomNumber(int numberGuessedByUser){
		return numberGuessedByUser != generatedRandomNumber;
	}
	
	
	private static boolean numberGuessedByUserEqualsToGeneratedRandomNumber(int numberGuessedByUser){
		return numberGuessedByUser == generatedRandomNumber;
	}
	
	private static boolean numberGuessedByUserIsMoreThanGeneratedRandomNumber(int numberGuessedByUser) {
		return numberGuessedByUser > generatedRandomNumber;
	}
	
	private static boolean numberGuessedByUserIsLessThanGeneratedRandomNumber(int numberGuessedByUser) {
		return numberGuessedByUser < generatedRandomNumber;
	}
	
	private static String getFeedbackMessageForUserGuessIsCorrect() {
			return "Congragulations! Your guess is correct! You took "+numberOfGuesses+" guesses.";
	}
	
	private static String getFeedbackMessageForNumberGuessedByUserTooHigh() {
		return "Incorrect answer. Guess is too high please try again.";
	}
	
	private static String getFeedbackMessageForNumberGuessedByUserTooLow() {
		return "Incorrect answer. Guess is too low please try again.";
	}
	
	private static void showFeedbackMessageToUser(String feedbackMessageForUser) {
		System.out.println(feedbackMessageForUser);
	}
	
	
	

}



