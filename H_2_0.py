def calcul_h_way1(phi, ta, h_estim, pre):
    Pr = 0.69
    v = 0.00002076
    k = 0.03
    Dx = 1
    def appro_temperature(phi, ta, h_estim):
        tp = (ta + 273.15) + phi / h_estim
        tf_approx1 = (ta + (tp - 273.15)) / 2 + 273.15
        return tf_approx1
    def calcul_h_iteratif(Dx, k, Pr, v, phi, ta, h_estim):
        tp = (ta + 273.15) + phi / h_estim
        tf_approx1 = appro_temperature(phi, ta, h_estim)
        beta = 1 / tf_approx1
        Ra = Pr * (9.81 * beta * (Dx ** 3) * (tp - tf_approx1) / (v ** 2))
        if Ra > 10 ** 7:
            Nu = 0.1 * Ra ** (1 / 3)
            h = Nu * k / Dx
        else:
            Nu = 0.59 * Ra ** (1 / 4)
            h = Nu * k / Dx
        return h
    def h_en_fct_precision(pre, Dx, k, Pr, v, phi, ta, h_estim):
        h = calcul_h_iteratif(Dx, k, Pr, v, phi, ta, h_estim)
        x = h - h_estim
        while abs(x) > pre:
            new_h = calcul_h_iteratif(Dx, k, Pr, v, phi, ta, h)
            x = h - new_h
            h = calcul_h_iteratif(Dx, k, Pr, v, phi, ta, new_h)
        return h
    return h_en_fct_precision(pre,Dx,k,Pr,v,phi,ta,h_estim)
print (calcul_h_way1(420,30,4,0.00001))
