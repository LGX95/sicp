;;; max-and-min.scm

(define (max x y)
  (if (< x y)
      y
      x))

(define (mix x y)
  (if (< x y)
      x
      y))
