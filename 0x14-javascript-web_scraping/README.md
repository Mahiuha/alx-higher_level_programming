# Javascript - Web scraping

Javascripts interpretted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [node v6.10.2](https://nodejs.org/en/blog/release/v6.10.2/) and must conform to [semistandard](https://github.com/Flet/semistandard) style.

### Focus
How to use [request](https://github.com/request/request) to query APIs in Javascript. How to manipulate JSON data in Javascript. Learn to read and write to files using [fs](https://nodejs.org/api/fs.html#fs_file_paths).

### Example Usages

[0-readme.js](0-readme.js)
```
0x14-javascript-web_scraping:$ ./0-readme.js cisfun
C is super fun!
0x14-javascript-web_scraping:$ cat cisfun
C is super fun!
0x14-javascript-web_scraping:$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
0x14-javascript-web_scraping:$ 
```
[1-writeme.js](1-writeme.js)
```
0x14-javascript-web_scraping:$ ./1-writeme.js my_file.txt "Python is cool"
0x14-javascript-web_scraping:$ cat my_file.txt ; echo ""
Python is cool
0x14-javascript-web_scraping:$ 
```
[2-statuscode.js](2-statuscode.js)
```
0x14-javascript-web_scraping:$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
0x14-javascript-web_scraping:$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
0x14-javascript-web_scraping:$ 
```
[3-starwars_title.js](3-starwars_title.js)
```
0x14-javascript-web_scraping:$ ./3-starwars_title.js 1
A New Hope
0x14-javascript-web_scraping:$ ./3-starwars_title.js 5
Attack of the Clones
0x14-javascript-web_scraping:$ 
```
[4-starwars_count.js](4-starwars_count.js)
```
0x14-javascript-web_scraping:$ ./4-starwars_count.js http://swapi.co/api/films
3
0x14-javascript-web_scraping:$ 
```
[5-request_store.js](5-request_store.js)
```
0x14-javascript-web_scraping:$ ./5-request_store.js http://loripsum.net/api loripsum
0x14-javascript-web_scraping:$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>

0x14-javascript-web_scraping:$ 
```
[6-completed_tasks.js](6-completed_tasks.js)
```
0x14-javascript-web_scraping:$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
0x14-javascript-web_scraping:$ 
```
[100-starwars_characters.js](100-starwars_characters.js)
```
0x14-javascript-web_scraping:$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
0x14-javascript-web_scraping:$ 
```
[101-starwars_characters.js](101-starwars_characters.js)
```
0x14-javascript-web_scraping:$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
0x14-javascript-web_scraping:$ 
```
### Author
- [Joseph Mahiuha](https://github.com/Mahiuha)
### Acknowledgments
- [ALX](https://www.alxafrica.com/)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- [Loripsum API](http://loripsum.net/api)
- [Star Wars API](https://swapi.co/)
- [Twitter API](https://developer.twitter.com/en/docs)
