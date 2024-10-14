% Derivadas de constantes
derivar(C, 0) :- number(C).

% Derivada de la variable x
derivar(x, 1).

% Regla de la suma: d(f + g) / dx = d(f)/dx + d(g)/dx
derivar(F + G, DF + DG) :-
    derivar(F, DF),
    derivar(G, DG).

% Regla de la resta: d(f - g) / dx = d(f)/dx - d(g)/dx
derivar(F - G, DF - DG) :-
    derivar(F, DF),
    derivar(G, DG).

% Regla del producto: d(f * g) / dx = f' * g + f * g'
derivar(F * G, F * DG + DF * G) :-
    derivar(F, DF),
    derivar(G, DG).

% Regla del cociente: d(f / g) / dx = (f' * g - f * g') / (g^2)
derivar(F / G, (DF * G - F * DG) / (G * G)) :-
    derivar(F, DF),
    derivar(G, DG).

% Derivada de potencias de expresiones generales
derivar(F^N, N * F^(N-1) * DF) :-
    number(N),
    derivar(F, DF).

% Derivada de funciones trigonométricas
derivar(sin(F), cos(F) * DF) :- derivar(F, DF).
derivar(cos(F), -sin(F) * DF) :- derivar(F, DF).
derivar(tan(F), (1 + tan(F)^2) * DF) :- derivar(F, DF).

% Derivada de arcotangente
derivar(arctan(F), DF / (1 + F^2)) :-
    derivar(F, DF).

% Derivada de exponencial
derivar(exp(F), exp(F) * DF) :- derivar(F, DF).

% Derivada de logaritmo natural
derivar(ln(F), DF / F) :- derivar(F, DF).

% Regla de la cadena para funciones compuestas: d(f(g(x))) = f'(g(x)) * g'(x)
derivar(comp(F, G), DF_G * DG) :-
    derivar(F, DF),
    derivar(G, DG),
    sustituir(G, DF, DF_G).

% Sustituir la variable x por G en una expresión
sustituir(x, G, G).
sustituir(F + H, G, FG + HG) :-
    sustituir(F, G, FG),
    sustituir(H, G, HG).
sustituir(F - H, G, FG - HG) :-
    sustituir(F, G, FG),
    sustituir(H, G, HG).
sustituir(F * H, G, FG * HG) :-
    sustituir(F, G, FG),
    sustituir(H, G, HG).
sustituir(F / H, G, FG / HG) :-
    sustituir(F, G, FG),
    sustituir(H, G, HG).
sustituir(sin(F), G, sin(FG)) :- sustituir(F, G, FG).
sustituir(cos(F), G, cos(FG)) :- sustituir(F, G, FG).
sustituir(exp(F), G, exp(FG)) :- sustituir(F, G, FG).
sustituir(ln(F), G, ln(FG)) :- sustituir(F, G, FG).
