import javax.imageio.ImageIO;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class ColoredToBlackAndWhite {


	public static void main(String[] args) throws IOException {
	
		BufferedImage image = ImageIO.read(new File("test.jpg"));
		BufferedImage blackAndWhite = new BufferedImage(image.getWidth(), image.getHeight(), BufferedImage.TYPE_BYTE_GRAY);
		Graphics2D g2 = blackAndWhite.createGraphics();
		g2.drawRenderedImage(image, null);
		ImageIO.write(blackAndWhite, "jpg", new File("testing.jpg"));
	
	}
		
}
	
	