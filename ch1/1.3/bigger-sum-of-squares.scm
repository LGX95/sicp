;;; bigger-sum-of-squares.scm

(load "p8-sum-of-squares.scm")
(load "max-and-min.scm")

(define (bigger-sum-of-squares x y z)
  (sum-of-squares (max x y)
              (max (min x y)
                   z)))
