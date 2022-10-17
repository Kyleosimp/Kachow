import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.nio.file.Files;

public class Main {
    public static String readFileAsString(String fileName)throws Exception
    {
        String data = "";
        data = new String(Files.readAllBytes(java.nio.file.Paths.get(fileName)));
        return data;
    }
    public static void main(String[] args) throws Exception {
        //replace the file path with your own
        String data = readFileAsString("src/zincFinger.txt");
        //header regex
        String header_regex = ".+zinc finger.+";
        Pattern header_pattern = Pattern.compile(header_regex);
        Matcher header_matcher = header_pattern.matcher(data);
        //body regex
        //replace the regex with your own found on lines 21 and 25 in the brackets
        String body_regex = "[FSYCWLPHQRIMTNKVADEG\n]+C[FSYCWLPHQRIMTNKVADEG\n]{2}C[FSYCWLPHQRIMTNKVADEG\n]{17}C[FSYCWLPHQRIMTNKVADEG\n]{2}C[FSYCWLPHQRIMTNKVADEG\n]+";
        Pattern body_pattern = Pattern.compile(body_regex);
        Matcher body_matcher = body_pattern.matcher(data);
        //zinc finger regex
        //replace the regex with your own found on lines 21 and 25 in the brackets
        String zinc_regex = "C[FSYCWLPHQRIMTNKVADEG\n]{2}C[FSYCWLPHQRIMTNKVADEG\\n]{17}C[FSYCWLPHQRIMTNKVADEG\\n]{2}C";
        Pattern zinc_pattern = Pattern.compile(zinc_regex);
        Matcher zinc_matcher = zinc_pattern.matcher(data);
        //find and print your outputs with proper formatting using a for while loop
        while (body_matcher.find() && header_matcher.find() && zinc_matcher.find()) {
            //print statements
            System.out.printf("%s" + "\n", header_matcher.group());
            System.out.printf("Contains the zinc finger site: " + "%s" + "\n", zinc_matcher.group());
            System.out.print("at locations: " + body_matcher.group().indexOf(zinc_matcher.group()) + " ");
            int index_position = body_matcher.group().indexOf(zinc_matcher.group());
            int index_length = zinc_matcher.group().length();
            System.out.println(index_position + index_length);
            //split the body_matcher.group() into an array of strings
            String[] body_array = body_matcher.group().split(
                    "\n");
            //find the new index position of the zinc_matcher.group() in the body_array
            int new_index_position = 0;
            for (int i = 0; i < body_array.length; i++) {
                if (body_array[i].contains(zinc_matcher.group())) {
                    new_index_position = i;
                    break;
                }
            }
            //find the new index length of the zinc_matcher.group() in the body_array
            int new_index_length = 0;
            for (int i = 0; i < body_array.length; i++) {
                if (body_array[i].contains(zinc_matcher.group())) {
                    new_index_length = body_array[i].indexOf(zinc_matcher.group()) + zinc_matcher.group().length();
                    break;
                }
            }
            //print the body_matcher.group() with a line of spaces between each line, stop at the zinc_matcher.group()
            for (int i = 0; i < new_index_position; i++) {
                System.out.println(body_array[i]);
                System.out.println();
                }
            //continue printing the body_matcher.group() with a line of spaces between each line, start at the zinc_matcher.group()
            for (int i = new_index_position; i < body_array.length; i++) {
                System.out.println(body_array[i]);
                //highlight the zinc finger site with asterisks
                if (body_array[i].contains(zinc_matcher.group())) {
                    for (int j = 0; j < new_index_length; j++) {
                        if (j < body_array[i].indexOf(zinc_matcher.group())) {
                            System.out.print(" ");
                        } else {
                            System.out.print("*");
                        }
                    }
                    // if asterisks are the last line before the next header, print a line of spaces
                    if (i == body_array.length - 1) {
                        System.out.println();
                    }
                }
                System.out.println();
            }
        }
    }
}