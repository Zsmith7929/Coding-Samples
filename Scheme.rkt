#lang scheme

;binomial(n,k): if k=1 or n=k return 1; if 0<k<N is false return 'error
(define (binomial N k)
        (if (= k 0) 1
            (if (= N k) 1
                (if (> 0 k) 'error
                    (if (> k N) 'error
                        (+ (binomial (- N 1) (- k 1)) (binomial (- N 1) k)))))))


(define (mod N M)
        (if (< (* N N) (* M M)) N
            (if (< N 0) (mod (+ N M) M)
                (mod (- N M) M))))


(define (binaryToDecimal b)
        (if (= b 0) b
            (+ (mod b 10) (* (binaryToDecimal (- (/ b 10) (/ (mod b 10) 10))) 2))))


(define (addBinary binaryList)
        (if (null? binaryList) 0
        (+ (binaryToDecimal (car binaryList)) (addBinary (cdr binaryList)))))


(define (min list)
        (if (null? list) null
            (if (null? (cdr list)) (car list)
                (if (< (car list) (car (cdr list))) (min (cdr list))
                    (min (cons (car list) (cdr (cdr list))))))))


(define (myRemove atm list)
        (if (null? list) list
            (if (eq? atm list) empty
                (if (pair? list)
                    (if (eq? (car list) atm) (myRemove atm (cdr list))
                        (cons (myRemove atm (car list)) (myRemove atm (cdr list))))
                    list))))


(define (selectionSort list)
        (if (null? list) null
            (let ([x (min list)])
                (if (null? x) x
                (cons (selectionSort (myRemove x list)) x)))))


"binomial test"
(binomial 4 0)
(binomial 8 8)
(binomial 3 2)
(binomial 7 4)

"mod test"
(mod 9 5)
(mod 7 9)
(mod 100 37)
(mod 20 5)
(mod -11 3)

"binaryToDecimal test"
(binaryToDecimal 0)
(binaryToDecimal 1011)
(binaryToDecimal 111111)
(binaryToDecimal 10001)

"addBinary test"
(addBinary '(1101 111 10 101))
(addBinary '(0))
(addBinary '(11011))

"min test"
(min '(4 5 1 2 5))
(min '(3))
(min '())
(min '(5 5 5))

"myRemove test"
(myRemove 'a '())
(myRemove 'a '(a))
(myRemove 'a '(a b c d a b a a))
(myRemove 'a '(x y z))
(myRemove 'a '(a (x y z) (r s t a)))
(myRemove 'a '(((a (l a) b) a) m a))

"selectionSort test"
(selectionSort '())
(selectionSort '(5))
(selectionSort '(6 10 23 12 2 9 18 1 0 15))
(selectionSort '(3 4 7 3 7 7 4 3 2 3 7))
