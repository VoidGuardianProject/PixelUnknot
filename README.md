--------------------- Disclaimer ---------------------
   This software is provided by the author and
   contributors ``as is'' and any express or implied
   warranties, including, but not limited to, the
   implied warranties of merchantability and
   fitness for a particular purpose are dis-
   claimed. In no event shall the author or con-
   tributors be liable for any direct, indirect,
   incidental, special, exemplary, or consequen-
   tial damages (including, but not limited to,
   procurement of substitute goods or services;
   loss of use, data, or profits; or business
   interruption) however caused and on any
   theory of liability, whether in contract,
   strict liability, or tort (including negligence
   or otherwise) arising in any way out of the use
   of this software, even if advised of the poss-
   ibility of such damage.
--------------------------------------------------------

This repo provides decryption tools


gather.sh will download all the jpeg from a forum thread,
detect any pk headers and copy that picture into matches
It is used like such

```
gather.sh <domain> <board> <thread-id>
gather.sh half.org v 123
```

To detect the pk header, we run:
```
python detect.py Q4example.jpg
```

Build the java code with maven to crack/generate .coeff file for image with PixelUnknot java.

The `brutef5` folder is C code to brute force crack the f5 algo
The `brutef5cuda` folder is nvidia gpu version C code to brute force crack the f5 algo.

Other tools:
See other of our repos for other tools:
One such example is the f5 library which can be run as

```
java -jar f5.jar x -p plan -o message.txt Q4example.jpg
```
