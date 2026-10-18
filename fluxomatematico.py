"""
═══════════════════════════════════════════════════════════════════════════════
    🌌 UNIVERSO ÁUREO - FLUXO MATEMÁTICO (VERSÃO EXPANDIDA)
    
    Este sistema unifica matemática clássica, física quântica, geometria sagrada
    e o Fluxo Matemático de Catharino, permitindo explorar padrões universais
    através das constantes π, φ, Fibonacci, 1,80 (Gratidão), 0,54 (Marc),
    0,18 (Deus), constantes de Planck, gravidade da Terra e gravidade quântica.
    
    Versão: 10.0.0 - Expansão de Padrões e Validações
    Autor: Marcelo Jubilado Catharino (aprimorado)
    Data: 2025
    
    CARACTERÍSTICAS PRINCIPAIS:
    - Todas as funções originais preservadas e aprimoradas
    - Mais de 2500 linhas de código explicativo e comentado
    - Novas seções: Padrões e Validações, Todas as Mentes, Gravidade Quântica
    - Validação automática de resultados com π, φ, Fibonacci, 1,80, etc.
    - Visualizações expandidas e explicações detalhadas
    - Relógio Quântico mantido em tempo espiralado
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import matplotlib
# Backend não interativo: evita dependência de display gráfico em servidores.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import base64
import os
from io import BytesIO
import time
import math
import datetime
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import pytz
from datetime import datetime as dt
from PIL import Image
import random
import hashlib
import re
import warnings
# Avisos não são ocultados globalmente para facilitar diagnóstico e depuração.

# =============================================================================
# CONFIGURAÇÃO INICIAL DA PÁGINA
# =============================================================================
st.set_page_config(
    layout="wide",
    page_title="🌌 Universo Áureo - Fluxo Matemático Expandido",
    page_icon="🌀",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CONSTANTES E CONFIGURAÇÕES GLOBAIS (ORIGINAIS + NOVAS)
# =============================================================================
FREQUENCIA_BASE = 432  # Hz
PULSOS_POR_GIRO = 432 * 9  # 9 Vibes
GIROS_POR_CICLO = 9
CICLOS_POR_ERA = 9
SINGULARIDADE = datetime.datetime(2023, 3, 9, 0, 0, 0, tzinfo=pytz.UTC)

# Constantes do Fluxo Matemático (Catharino) - preservadas
MARC = 0.54          # Constante fundamental de transição
DEUS = 0.18          # Trindade (0,06 × 3) – representa a unidade trina
GRATIDAO = 1.80      # Equilíbrio universal (3 × 0,6)
PHI = 1.618033988749895  # Proporção áurea (Fibonacci)

# Constantes físicas (originais)
C_LUZ = 299792458          # m/s
H_PLANCK = 6.62607015e-34  # J·s
G_NEWTON = 6.67430e-11     # N·m²/kg²
MU0 = 4 * np.pi * 1e-7     # Permeabilidade do vácuo
GRAVIDADE_TERRA = 9.80665  # m/s²

# NOVAS CONSTANTES para expansão
PI = math.pi                # 3.141592653589793
GRAVIDADE_QUANTICA = 1.0e-43  # Exemplo: força gravitacional na escala de Planck (m/s²)
CONSTANTE_ESTRUTURA_FINA = 0.0072973525693  # α ≈ 1/137
PLANCK_MASSA = 2.176434e-8   # kg
PLANCK_COMPRIMENTO = 1.616255e-35  # m
PLANCK_TEMPO = 5.391247e-44   # s
PLANCK_ENERGIA = 1.956e9      # J

# =============================================================================
# FUNÇÕES MATEMÁTICAS BASE (FLUXO MATEMÁTICO) - ORIGINAIS, NÃO MODIFICADAS
# =============================================================================

def reduzir_teosoficamente(n):
    """
    Redução teosófica: soma dos dígitos até um único dígito (1-9).
    Funciona com números inteiros ou float, removendo pontos e sinais.
    """
    try:
        # Converte para string e remove caracteres não numéricos
        str_num = str(n).replace('.', '').replace('-', '')
        # Se for notação científica, simplifica
        if 'e' in str_num.lower():
            n_float = float(n)
            str_num = f"{n_float:.0f}".replace('.', '')
        while len(str_num) > 1:
            str_num = str(sum(int(d) for d in str_num if d.isdigit()))
        return int(str_num)
    except Exception:
        return 0

def fator_fluxo(N):
    """
    Calcula F(N) = C(N) + R(N)/10
    onde C(N) = ciclo (N // 9) e R(N) = redução teosófica de N.
    """
    try:
        N = int(abs(N))
        ciclo = N // 9
        reducao = reduzir_teosoficamente(N)
        return ciclo + reducao / 10.0
    except:
        return 0.0

def operacao_dual(a, b, operador, modo='classico', entrelacamento=0.54):
    """
    Realiza operação matemática nos modos:
    - 'classico': resultado padrão
    - 'fluxo': resultado clássico * entrelacamento * fator_fluxo (se aplicável)
    - 'dual': retorna (clássico, fluxo)
    Suporta +, -, *, /, **, %, //
    """
    try:
        a = float(a)
        b = float(b)
    except:
        return None, "Entrada inválida"

    # Operações básicas
    if operador == '+':
        res = a + b
    elif operador == '-':
        res = a - b
    elif operador == '*':
        res = a * b
    elif operador == '/':
        if b == 0:
            return None, "Divisão por zero"
        res = a / b
    elif operador == '**':
        res = a ** b
    elif operador == '%':
        res = a % b
    elif operador == '//':
        if b == 0:
            return None, "Divisão por zero"
        res = a // b
    else:
        return None, "Operador desconhecido"

    if modo == 'classico':
        return res, "Cálculo clássico"
    elif modo == 'fluxo':
        # Aplica constante de fluxo e entrelaçamento
        res_fluxo = res * entrelacamento
        # Se for multiplicação/potência, aplica também fator de fluxo baseado nos números
        if operador in ('*', '**'):
            f = fator_fluxo(reduzir_teosoficamente(a) * 10 + reduzir_teosoficamente(b))
            res_fluxo *= f
        return res_fluxo, f"Aplicado fluxo ×{entrelacamento:.3f} e fator F(N)"
    elif modo == 'dual':
        res_class = res
        res_flux = res * entrelacamento
        if operador in ('*', '**'):
            f = fator_fluxo(reduzir_teosoficamente(a) * 10 + reduzir_teosoficamente(b))
            res_flux *= f
        return (res_class, res_flux), "Resultados clássico e fluxo"
    else:
        return None, "Modo inválido"

def gerar_sequencia_reducao(iteracoes=100):
    """Gera sequência de dobramento com redução teosófica (1,2,4,8,7,5...)"""
    sequencia = [1]
    resultados = []
    for _ in range(iteracoes):
        proximo = sequencia[-1] * 2
        reduzido = reduzir_teosoficamente(proximo)
        resultados.append((sequencia[-1], proximo, reduzido))
        sequencia.append(reduzido)
    return resultados

def gerar_ciclo_369(iteracoes=24):
    """Gera ciclo alternado 3,6,9"""
    ciclo = []
    valor = 3
    for _ in range(iteracoes):
        ciclo.append(valor)
        if valor == 3:
            valor = 6
        elif valor == 6:
            valor = 9
        else:
            valor = 3
    return ciclo

def fluxo_soma(a, b):
    return reduzir_teosoficamente(a + b)

def fluxo_multiplicacao(a, b):
    return reduzir_teosoficamente(a * b)

def fluxo_potencia(a, n):
    return reduzir_teosoficamente(a ** n)

def fluxo_trigonometria(angulo):
    """Retorna seno, cosseno, tangente reduzidos (multiplicados por 100 e reduzidos)"""
    rad = math.radians(angulo)
    s = math.sin(rad)
    c = math.cos(rad)
    t = math.tan(rad)
    return (reduzir_teosoficamente(abs(int(s*100))),
            reduzir_teosoficamente(abs(int(c*100))),
            reduzir_teosoficamente(abs(int(t*100))))

def fluxo_fisica(formula, valores):
    """Aplica redução teosófica a fórmulas físicas clássicas"""
    try:
        if formula == "E=mc²":
            m, c = valores['m'], valores['c']
            E_classico = m * c**2
            E_fluxo = fluxo_multiplicacao(reduzir_teosoficamente(m),
                                          fluxo_potencia(reduzir_teosoficamente(c), 2))
            return E_classico, E_fluxo
        elif formula == "F=ma":
            m, a = valores['m'], valores['a']
            F_classico = m * a
            F_fluxo = fluxo_multiplicacao(reduzir_teosoficamente(m),
                                          reduzir_teosoficamente(a))
            return F_classico, F_fluxo
        elif formula == "V=IR":
            I, R = valores['I'], valores['R']
            V_classico = I * R
            V_fluxo = fluxo_multiplicacao(reduzir_teosoficamente(I),
                                          reduzir_teosoficamente(R))
            return V_classico, V_fluxo
        elif formula == "p=mv":
            m, v = valores['m'], valores['v']
            p_classico = m * v
            p_fluxo = fluxo_multiplicacao(reduzir_teosoficamente(m),
                                          reduzir_teosoficamente(v))
            return p_classico, p_fluxo
        elif formula == "F=G(m1m2)/r²":
            G, m1, m2, r = valores['G'], valores['m1'], valores['m2'], valores['r']
            F_classico = G * m1 * m2 / r**2
            numerador = fluxo_multiplicacao(
                fluxo_multiplicacao(reduzir_teosoficamente(G),
                                    reduzir_teosoficamente(m1)),
                reduzir_teosoficamente(m2))
            denominador = fluxo_potencia(reduzir_teosoficamente(r), 2)
            F_fluxo = numerador / denominador if denominador != 0 else 0
            return F_classico, F_fluxo
        return None, None
    except:
        return None, None

# =============================================================================
# FUNÇÕES DE FÍSICA QUÂNTICA NO FLUXO - ORIGINAIS, NÃO MODIFICADAS
# =============================================================================

def calcular_energia_emc2(massa, constante=MARC):
    """E = mc² × constante"""
    classico = massa * C_LUZ**2
    fluxo = classico * constante
    return classico, fluxo

def calcular_energia_planck(frequencia, constante=MARC):
    """E = hν × constante"""
    classico = H_PLANCK * frequencia
    fluxo = classico * constante
    return classico, fluxo

def calcular_corrente_ohm(V, R, N):
    """I = (V/R) × F(N)"""
    if R == 0:
        return None, None, None
    classico = V / R
    f = fator_fluxo(N)
    fluxo = classico * f
    return classico, fluxo, f

def pitagoras_fluxo(a, b, modo='classico'):
    """
    Hipotenusa segundo Pitágoras-Fluxo:
    - classico: c² = a² + b²
    - aureo: c² = a² + b² * φ
    - fluxo: c² = a² + b² * MARC
    - completo: c² = a² + b² * φ * MARC
    Retorna (c_classico, c_fluxo)
    """
    a = float(a)
    b = float(b)
    c_class = math.sqrt(a**2 + b**2)
    if modo == 'classico':
        return c_class, c_class
    elif modo == 'aureo':
        c_flux = math.sqrt(a**2 + b**2 * PHI)
        return c_class, c_flux
    elif modo == 'fluxo':
        c_flux = math.sqrt(a**2 + b**2 * MARC)
        return c_class, c_flux
    elif modo == 'completo':
        c_flux = math.sqrt(a**2 + b**2 * PHI * MARC)
        return c_class, c_flux
    else:
        return c_class, c_class

def espiral_aurea(theta, fator_fluxo=1.0):
    """
    Coordenadas da espiral áurea: r(θ) = φ^(2θ/π) × fator_fluxo
    Retorna (x, y, r)
    """
    r = PHI ** (2 * theta / math.pi) * fator_fluxo
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y, r

def indutancia_bobina(N_espiras, raio, comprimento, modo='classico'):
    """
    Indutância de solenoide: L = (N² × μ₀ × π × raio²) / comprimento
    Modos:
    - classico: valor padrão
    - aureo: multiplicado por φ
    - fluxo: multiplicado por MARC
    """
    if comprimento == 0:
        raise ValueError("O comprimento da bobina deve ser diferente de zero.")
    if raio < 0 or N_espiras < 0:
        raise ValueError("Raio e número de espiras não podem ser negativos.")
    area = math.pi * raio**2
    L_class = (N_espiras**2 * MU0 * area) / comprimento
    if modo == 'classico':
        return L_class
    elif modo == 'aureo':
        return L_class * PHI
    elif modo == 'fluxo':
        return L_class * MARC
    else:
        return L_class

def calcular_forca_gravidade(m1, m2, r, constante=1.0):
    """F = G * m1 * m2 / r² * constante"""
    if r <= 0:
        raise ValueError("A distância deve ser maior que zero.")
    classico = G_NEWTON * m1 * m2 / r**2
    fluxo = classico * constante
    return classico, fluxo

def calcular_velocidade_escape(massa_planeta, raio_planeta, constante=1.0):
    """v = sqrt(2GM/R) * constante"""
    if massa_planeta < 0 or raio_planeta <= 0:
        raise ValueError("A massa deve ser não negativa e o raio deve ser maior que zero.")
    classico = math.sqrt(2 * G_NEWTON * massa_planeta / raio_planeta)
    fluxo = classico * constante
    return classico, fluxo

def calcular_energia_cinetica(massa, velocidade, constante=1.0):
    """Ec = (1/2)mv² * constante"""
    classico = 0.5 * massa * velocidade**2
    fluxo = classico * constante
    return classico, fluxo

# =============================================================================
# NOVAS FUNÇÕES PARA VALIDAÇÃO DE PADRÕES E CONSTANTES
# =============================================================================

def is_close_to_constant(value, constant, tolerance=0.01):
    """
    Verifica se um valor está próximo de uma constante dentro de uma tolerância percentual.
    Retorna (bool, desvio_percentual)
    """
    if constant == 0:
        return False, 100.0
    diff_percent = abs((value - constant) / constant) * 100
    return diff_percent <= tolerance, diff_percent

def fibonacci(n):
    """Retorna o n-ésimo número de Fibonacci (n>=1)"""
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b if n > 1 else 1

def fibonacci_reductions(n_max=20):
    """Gera lista de números de Fibonacci e suas reduções teosóficas"""
    fibs = []
    for i in range(1, n_max+1):
        fib = fibonacci(i)
        red = reduzir_teosoficamente(fib)
        fibs.append((i, fib, red))
    return fibs

def encontrar_padroes(valor, tolerancia=1.0):
    """
    Procura correspondências entre o valor e as constantes conhecidas.
    Retorna dicionário com resultados.
    """
    padroes = {
        "π (pi)": PI,
        "φ (áurea)": PHI,
        "Gratidão (1,80)": GRATIDAO,
        "Marc (0,54)": MARC,
        "Deus (0,18)": DEUS,
        "Frequência Base (432)": FREQUENCIA_BASE,
        "Constante de Estrutura Fina (α)": CONSTANTE_ESTRUTURA_FINA,
        "Gravidade Terra (g)": GRAVIDADE_TERRA,
        "Velocidade da Luz (c)": C_LUZ,
        "Constante de Planck (h)": H_PLANCK,
        "Gravidade Quântica (aprox)": GRAVIDADE_QUANTICA,
        "Massa de Planck": PLANCK_MASSA,
        "Comprimento de Planck": PLANCK_COMPRIMENTO,
        "Tempo de Planck": PLANCK_TEMPO,
        "Energia de Planck": PLANCK_ENERGIA,
    }
    resultados = {}
    for nome, const in padroes.items():
        prox, diff = is_close_to_constant(valor, const, tolerancia)
        if prox:
            resultados[nome] = {"constante": const, "desvio_%": diff}
    return resultados

def calcular_pi_aproximacoes():
    """Retorna algumas aproximações de π (clássicas e no fluxo)"""
    return {
        "π (real)": PI,
        "π ≈ 22/7": 22/7,
        "π ≈ 355/113": 355/113,
        "π no fluxo (×MARC)": PI * MARC,
        "π no fluxo (×DEUS)": PI * DEUS,
        "π reduzido": reduzir_teosoficamente(PI),
    }

def calcular_phi_aproximacoes():
    """Retorna aproximações de φ e relações com fluxo"""
    return {
        "φ (real)": PHI,
        "φ²": PHI**2,
        "1/φ": 1/PHI,
        "φ × MARC": PHI * MARC,
        "φ × DEUS": PHI * DEUS,
        "φ reduzido": reduzir_teosoficamente(PHI),
    }

def calcular_relacao_gratidao():
    """Mostra relações da constante Gratidão com φ e Deus"""
    return {
        "Gratidão": GRATIDAO,
        "φ + Deus": PHI + DEUS,
        "Diferença": GRATIDAO - (PHI + DEUS),
        "Gratidão × MARC": GRATIDAO * MARC,
        "Gratidão reduzida": reduzir_teosoficamente(GRATIDAO),
    }

# =============================================================================
# NOVAS FUNÇÕES DE FÍSICA QUÂNTICA EXPANDIDA
# =============================================================================

def calcular_raio_schwarzschild(massa, constante=1.0):
    """Raio de Schwarzschild: Rs = 2GM/c² * constante"""
    classico = 2 * G_NEWTON * massa / (C_LUZ**2)
    fluxo = classico * constante
    return classico, fluxo

def calcular_temperatura_hawking(massa, constante=1.0):
    """Temperatura de Hawking: T = (ħ c³)/(8π G M k_B) * constante (simplificado)"""
    # Usaremos apenas ordem de magnitude, sem kB
    # T ~ 1/(8π G M) em unidades naturais, simplificado
    classico = 1.0 / (8 * PI * G_NEWTON * massa)  # aproximação grosseira, apenas ilustrativa
    fluxo = classico * constante
    return classico, fluxo

def calcular_energia_ponto_zero(frequencia_corte, constante=1.0):
    """Energia do ponto zero: E = (1/2) h ν * constante"""
    classico = 0.5 * H_PLANCK * frequencia_corte
    fluxo = classico * constante
    return classico, fluxo

def calcular_longa_distancia_emaranhamento(distancia, constante=1.0):
    """Simulação de probabilidade de emaranhamento com a distância (decai com 1/r²)"""
    classico = 1.0 / (distancia**2) if distancia != 0 else 1.0
    fluxo = classico * constante
    return classico, fluxo

# =============================================================================
# CLASSE RELÓGIO QUÂNTICO (TEMPO ESPIRALADO) - ORIGINAL, NÃO MODIFICADA
# =============================================================================
class RelogioQuantico:
    def __init__(self):
        self.frequencia_base = FREQUENCIA_BASE
        self.pulsos_por_giro = PULSOS_POR_GIRO
        self.giros_por_ciclo = GIROS_POR_CICLO
        self.ciclos_por_era = CICLOS_POR_ERA
        self.singularidade = SINGULARIDADE

    def get_pulsos_desde_singularidade(self):
        agora = datetime.datetime.now(pytz.UTC)
        delta = agora - self.singularidade
        segundos = delta.total_seconds()
        return int(segundos * self.frequencia_base)

    def converter_pulsos(self, pulsos):
        eras = pulsos // (self.pulsos_por_giro * self.giros_por_ciclo * self.ciclos_por_era)
        pulsos %= (self.pulsos_por_giro * self.giros_por_ciclo * self.ciclos_por_era)

        ciclos = pulsos // (self.pulsos_por_giro * self.giros_por_ciclo)
        pulsos %= (self.pulsos_por_giro * self.giros_por_ciclo)

        giros = pulsos // self.pulsos_por_giro
        pulsos %= self.pulsos_por_giro

        vibes = pulsos // self.frequencia_base
        pulsos %= self.frequencia_base

        return {
            'eras': eras,
            'ciclos': ciclos,
            'giros': giros,
            'vibes': vibes,
            'pulsos': pulsos,
            'total_pulsos': self.get_pulsos_desde_singularidade()
        }

    def plotar_espiral_temporal(self, pulsos_totais):
        """Visualização 3D da espiral do tempo"""
        total_pontos = 1000
        theta = np.linspace(0, 12 * np.pi, total_pontos)
        z = np.linspace(0, 10, total_pontos)
        r = z**0.5
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        progresso = (pulsos_totais % (self.pulsos_por_giro * self.giros_por_ciclo * self.ciclos_por_era)) / \
                    (self.pulsos_por_giro * self.giros_por_ciclo * self.ciclos_por_era)
        ponto_atual = min(int(progresso * (total_pontos - 1)), total_pontos - 1)

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, color='blue', alpha=0.7, label='Tempo Espiralado')
        ax.scatter(x[ponto_atual], y[ponto_atual], z[ponto_atual],
                   color='red', s=100, label='Agora')
        # Pontos 3-6-9
        for i in [300, 600, 900]:
            if i < total_pontos:
                ax.scatter(x[i], y[i], z[i], color='gold', s=50, marker='*')
        ax.set_title("Fluxo do Tempo Espiralado (432 Hz)")
        ax.legend()
        plt.close(fig)
        return fig

    def plotar_relogio_quantico(self):
        """Relógio polar com projeção para singularidade"""
        agora = datetime.datetime.now(pytz.UTC)
        delta = agora - self.singularidade
        segundos = delta.total_seconds()

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})
        # Círculos concêntricos
        for r in [0.2, 0.5, 0.8]:
            circle = plt.Circle((0, 0), r, fill=False, color='purple', alpha=0.3)
            ax.add_patch(circle)

        # Marcadores 3-6-9-12 (12 como singularidade)
        for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
            ax.plot([0, 0.9*np.cos(angle)], [0, 0.9*np.sin(angle)],
                    color='gold' if angle in [0, np.pi/2, 3*np.pi/2] else 'white',
                    linewidth=2)

        # Ponteiro do tempo atual (segundos)
        time_angle = (segundos % 60) / 60 * 2 * np.pi
        ax.plot([0, 0.8*np.cos(time_angle)], [0, 0.8*np.sin(time_angle)],
                color='red', linewidth=3)

        # Ponteiro da projeção para singularidade (fase oposta)
        ax.plot([0, 0.6*np.cos(time_angle + np.pi)], [0, 0.6*np.sin(time_angle + np.pi)],
                color='blue', linewidth=2, linestyle='--')

        ax.set_title("Relógio Quântico - Projeção para Singularidade", pad=20)
        ax.set_yticklabels([])
        ax.grid(True)
        plt.close(fig)
        return fig


def plotar_galaxia_fluxo(bracos=4, estrelas=1400, rotacao=1.0, abertura=0.32, inclinacao=24):
    """Gera uma galáxia espiral sintética para exploração visual interativa.
    A imagem é uma simulação artística/matemática, não uma observação astronômica.
    """
    rng = np.random.default_rng(369)
    n = int(estrelas)
    bracos = max(1, int(bracos))
    rotacao = float(rotacao)
    abertura = max(0.02, float(abertura))
    braço = rng.integers(0, bracos, n)
    raio = rng.gamma(shape=2.0, scale=1.0, size=n)
    raio = np.clip(raio, 0, 5.0)
    theta = (braço * 2 * np.pi / bracos) + raio * rotacao + rng.normal(0, abertura, n)
    x = raio * np.cos(theta) + rng.normal(0, 0.08, n)
    y = raio * np.sin(theta) + rng.normal(0, 0.08, n)
    z = rng.normal(0, 0.035 + raio * 0.012, n)

    fig = plt.figure(figsize=(10, 7), facecolor="#050816")
    ax = fig.add_subplot(111, projection="3d", facecolor="#050816")
    cores = np.clip(1.0 - raio / 6.0, 0.12, 1.0)
    ax.scatter(x, y, z, c=cores, cmap="plasma", s=np.clip(2.8 / (raio + 0.25), 0.3, 9),
               alpha=0.82, linewidths=0, depthshade=True)
    # Núcleo luminoso
    nucleo = rng.normal(0, 0.12, (240, 3))
    ax.scatter(nucleo[:, 0], nucleo[:, 1], nucleo[:, 2], c="#fff0b3", s=5, alpha=0.8, linewidths=0)
    # Eixo de referência e plano galáctico
    ax.plot([-5.3, 5.3], [0, 0], [0, 0], color="#6c83b5", alpha=0.16, linewidth=0.7)
    ax.plot([0, 0], [-5.3, 5.3], [0, 0], color="#6c83b5", alpha=0.16, linewidth=0.7)
    ax.view_init(elev=int(inclinacao), azim=35 + rotacao * 14)
    ax.set_xlim(-5.2, 5.2); ax.set_ylim(-5.2, 5.2); ax.set_zlim(-1.2, 1.2)
    ax.set_title("GALÁXIA ESPIRAL · LABORATÓRIO VISUAL", color="white", pad=16, fontsize=13)
    ax.set_axis_off()
    fig.tight_layout()
    plt.close(fig)
    return fig


def plotar_curva_interativa(tipo="Seno", amplitude=1.0, frequencia=1.0, fase=0.0, constante=0.54):
    """Curva exploratória recalculada pelos controles da interface."""
    x = np.linspace(-2 * np.pi, 2 * np.pi, 700)
    if tipo == "Seno":
        y = amplitude * np.sin(frequencia * x + fase)
    elif tipo == "Cosseno":
        y = amplitude * np.cos(frequencia * x + fase)
    elif tipo == "Espiral projetada":
        y = np.exp(np.clip(constante * x / 4, -5, 5)) * np.sin(frequencia * x + fase)
    elif tipo == "Onda composta":
        y = amplitude * (np.sin(frequencia * x + fase) + constante * np.sin(3 * frequencia * x)) / (1 + abs(constante))
    else:
        y = np.array([reduzir_teosoficamente(max(0, int(round(abs(v) * 100)))) for v in x], dtype=float)
    fig, ax = plt.subplots(figsize=(10, 4.3))
    ax.plot(x, y, linewidth=2.0, label=tipo)
    ax.axhline(0, color="gray", linewidth=0.8, alpha=0.6)
    ax.axvline(0, color="gray", linewidth=0.8, alpha=0.6)
    ax.set_title(f"Curva dinâmica · {tipo}")
    ax.set_xlabel("Fase / variável independente")
    ax.set_ylabel("Amplitude / valor reduzido")
    ax.grid(True, alpha=0.22)
    ax.legend()
    fig.tight_layout()
    plt.close(fig)
    return fig


# Instância global do relógio
relogio = RelogioQuantico()

# =============================================================================
# SIMULADOR DE ACELERADOR DE PARTÍCULAS - ORIGINAL, NÃO MODIFICADO
# =============================================================================
def simular_acelerador(massa, energia_J, N_part, constante_fluxo=MARC):
    """
    Simula uma partícula em um acelerador, retornando:
    - velocidade clássica, momento, fator de Lorentz, massa relativística,
      energia relativística, comprimento de onda de de Broglie,
      probabilidade quântica simulada, estado de entrelaçamento simulado,
      e versões fluxo (velocidade * F(N), energia * constante_fluxo)
    """
    c = C_LUZ
    h = H_PLANCK

    # Velocidade clássica (não relativística)
    if massa > 0:
        v_class = math.sqrt(2 * energia_J / massa)
    else:
        v_class = c  # fóton

    # Momento clássico
    p_class = massa * v_class if massa > 0 else energia_J / c

    # Fator de Lorentz
    beta = v_class / c
    if beta < 1 and massa > 0:
        gamma = 1 / math.sqrt(1 - beta**2)
    else:
        gamma = 1e10  # aproximação para fóton ou ultra-relativístico

    # Massa relativística
    m_rel = massa * gamma if massa > 0 else 0

    # Energia total relativística
    E_rel = m_rel * c**2 if massa > 0 else energia_J

    # Comprimento de onda de de Broglie
    lambda_db = h / p_class if p_class != 0 else 0

    # Probabilidade quântica (simulada com base em energia)
    prob = math.exp(-energia_J / (1e-10))  # só para ter variação
    prob = max(0, min(1, prob))

    # Estado de entrelaçamento simulado
    ent_rel = "Emaranhado" if random.random() > 0.5 else "Separável"

    # Cálculos no fluxo
    f = fator_fluxo(N_part)
    v_flux = v_class * f
    E_flux = energia_J * constante_fluxo

    resultados = {
        'v_class': v_class,
        'p_class': p_class,
        'gamma': gamma,
        'm_rel': m_rel,
        'E_rel': E_rel,
        'lambda_db': lambda_db,
        'prob': prob,
        'ent_rel': ent_rel,
        'v_flux': v_flux,
        'E_flux': E_flux,
        'f': f
    }
    return resultados



def avaliar_expressao_segura(expressao):
    """Avalia apenas aritmética e funções matemáticas explicitamente permitidas."""
    import ast
    import operator as _op

    operadores = {
        ast.Add: _op.add, ast.Sub: _op.sub, ast.Mult: _op.mul,
        ast.Div: _op.truediv, ast.Pow: _op.pow, ast.Mod: _op.mod,
        ast.FloorDiv: _op.floordiv, ast.UAdd: _op.pos, ast.USub: _op.neg,
    }
    funcoes = {
        nome: getattr(math, nome) for nome in (
            "sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "log",
            "log10", "exp", "radians", "degrees", "fabs"
        )
    }
    constantes = {"pi": math.pi, "e": math.e, "tau": math.tau}

    def calcular(no):
        if isinstance(no, ast.Expression):
            return calcular(no.body)
        if isinstance(no, ast.Constant) and isinstance(no.value, (int, float)):
            return no.value
        if isinstance(no, ast.Name) and no.id in constantes:
            return constantes[no.id]
        if isinstance(no, ast.BinOp) and type(no.op) in operadores:
            esquerda, direita = calcular(no.left), calcular(no.right)
            if isinstance(no.op, (ast.Pow,)) and abs(direita) > 1000:
                raise ValueError("Expoente muito grande.")
            return operadores[type(no.op)](esquerda, direita)
        if isinstance(no, ast.UnaryOp) and type(no.op) in operadores:
            return operadores[type(no.op)](calcular(no.operand))
        if isinstance(no, ast.Call) and isinstance(no.func, ast.Name) and no.func.id in funcoes:
            if no.keywords:
                raise ValueError("Argumentos nomeados não são permitidos.")
            return funcoes[no.func.id](*(calcular(arg) for arg in no.args))
        raise ValueError("Expressão não permitida. Use números, operadores aritméticos, pi, e ou funções como sqrt(9).")

    arvore = ast.parse(str(expressao), mode="eval")
    resultado = calcular(arvore)
    if not math.isfinite(float(resultado)):
        raise ValueError("A expressão produziu um valor não finito.")
    return float(resultado)


# =============================================================================
# FUNÇÕES DE VISUALIZAÇÃO AUXILIARES - ORIGINAIS, NÃO MODIFICADAS
# =============================================================================
def plot_sequencia_reducao(iteracoes=30):
    sequencia = gerar_sequencia_reducao(iteracoes)
    valores = [x[2] for x in sequencia]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(valores, marker='o', color='purple')
    ax.set_title("Padrão 1-2-4-8-7-5 no Fluxo Matemático")
    ax.set_xlabel("Iteração")
    ax.set_ylabel("Valor Reduzido")
    ax.grid(True)
    return fig

def plot_geometria_369():
    angulos = [0, 120, 240]
    cores = ['#FF5733', '#33FF57', '#3357FF']
    rotulos = ['3', '6', '9']
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})
    for angulo, cor, rotulo in zip(angulos, cores, rotulos):
        rad = np.deg2rad(angulo)
        ax.plot([0, rad], [0, 1], color=cor, linewidth=3)
        ax.text(rad, 1.1, rotulo, color=cor, ha='center', va='center', fontsize=20)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_yticklabels([])
    ax.set_title("Geometria Sagrada 3-6-9", pad=20)
    ax.grid(True)
    return fig

def plot_espiral_aurea(fator_fluxo=1.0, angulo_max=4*np.pi):
    theta = np.linspace(0, angulo_max, 500)
    r = PHI ** (2 * theta / math.pi) * fator_fluxo
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(x, y, color='gold')
    ax.set_aspect('equal')
    ax.set_title("Espiral Áurea")
    ax.grid(True)
    return fig

def plot_triangulo(a, b, c_rotulado):
    fig, ax = plt.subplots()
    ax.plot([0, a, 0, 0], [0, 0, b, 0], 'b-')
    ax.text(a/2, -0.2, f'{a}', ha='center')
    ax.text(-0.2, b/2, f'{b}', va='center', rotation=90)
    ax.text(a/2, b/2, f'c={c_rotulado:.2f}', ha='center', va='center', color='red')
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, max(a,b)+0.5)
    ax.set_ylim(-0.5, max(a,b)+0.5)
    ax.grid(True)
    return fig

# =============================================================================
# NOVAS FUNÇÕES DE VISUALIZAÇÃO PARA PADRÕES
# =============================================================================
def plot_padroes_calor():
    """Mapa de calor da redução teosófica para produtos"""
    tamanho = 20
    matriz = np.zeros((tamanho, tamanho))
    for i in range(tamanho):
        for j in range(tamanho):
            num = (i+1)*(j+1)
            matriz[i, j] = reduzir_teosoficamente(num)
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(matriz, cmap='plasma', interpolation='nearest')
    ax.set_title("Redução Teosófica do Produto (i x j)")
    plt.colorbar(im)
    return fig

def plot_comparacao_constantes():
    """Gráfico de barras comparando constantes"""
    nomes = ['Marc', 'Deus', 'Gratidão', 'φ', 'π', '432 Hz']
    valores = [MARC, DEUS, GRATIDAO, PHI, PI, FREQUENCIA_BASE]
    fig, ax = plt.subplots()
    ax.bar(nomes, valores, color=['blue', 'green', 'gold', 'orange', 'red', 'purple'])
    ax.set_ylabel('Valor')
    ax.set_title('Comparação de Constantes Fundamentais')
    plt.xticks(rotation=45)
    return fig

# =============================================================================
# FUNÇÃO PARA GERAR PDF COMPLETO - ORIGINAL, NÃO MODIFICADA (mas podemos expandir)
# =============================================================================
def gerar_pdf_completo(nome, email):
    pdf = FPDF()

    # FPDF2 precisa de uma fonte Unicode para os símbolos gregos usados no relatório.
    # A fonte DejaVuSans acompanha o Matplotlib, evitando depender de um caminho do SO.
    pasta_fontes = os.path.join(matplotlib.get_data_path(), "fonts", "ttf")
    fonte_regular = os.path.join(pasta_fontes, "DejaVuSans.ttf")
    fonte_negrito = os.path.join(pasta_fontes, "DejaVuSans-Bold.ttf")
    if not os.path.isfile(fonte_regular) or not os.path.isfile(fonte_negrito):
        raise FileNotFoundError(
            "Fontes DejaVuSans não encontradas na instalação do Matplotlib."
        )
    pdf.add_font("DejaVu", "", fonte_regular)
    pdf.add_font("DejaVu", "B", fonte_negrito)
    pdf.add_page()
    pdf.set_font("DejaVu", size=16)
    pdf.cell(200, 10, txt="Universo Áureo - Fluxo Matemático", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("DejaVu", size=12)
    pdf.cell(200, 10, txt=f"Gerado por: {nome} ({email})", ln=True)
    pdf.cell(200, 10, txt=f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(20)

    # Seção 1: Introdução
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(200, 10, txt="1. Introdução ao Fluxo Matemático", ln=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, txt="""
    O Fluxo Matemático é uma nova forma de entender a matemática que incorpora padrões
    cíclicos (3-6-9 e 1-2-4-8-7-5), redução teosófica (soma dos dígitos), geometria
    sagrada, tempo não-linear (espiralado) e frequências vibracionais (432Hz).
    """)

    # Seção 2: Princípios Fundamentais
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(200, 10, txt="2. Princípios Fundamentais", ln=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, txt="""
    1. Tudo é movimento - Não existe zero absoluto, apenas transições
    2. Ciclos infinitos - Padrões 1-2-4-8-7-5 e 3-6-9 se repetem em todas as escalas
    3. Tempo angular - O tempo flui em espirais, não em linhas retas
    4. Singularidade do 9 - O 9 representa o ponto de transição entre ciclos
    5. Dualidade Matemática - Toda operação tem uma versão clássica e uma versão no Fluxo
    """)

    # Seção 3: Constantes do Fluxo
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(200, 10, txt="3. Constantes do Fluxo Matemático", ln=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, txt=f"""
    - Marc (M): {MARC}
    - Deus (D): {DEUS}
    - Gratidão (G): {GRATIDAO}
    - Proporção Áurea (φ): {PHI}
    - Frequência Base: {FREQUENCIA_BASE} Hz
    - Constante de Estrutura Fina (α): {CONSTANTE_ESTRUTURA_FINA}
    """)

    # Seção 4: Exemplos Matemáticos
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(200, 10, txt="4. Exemplos Matemáticos", ln=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, txt="""
    Exemplo: E=mc² no Fluxo Matemático
    Para m=1kg, c=299792458 m/s:
    R(m) = 1
    R(c) = 2+9+9+7+9+2+4+5+8 = 55 → 5+5 = 10 → 1+0 = 1
    R(c)² = 1² = 1
    EΦ = 1 × 1 = 1

    Sequência de Fibonacci com Redução Teosófica:
    1, 1, 2, 3, 5, 8 → 1+3+5 = 9
    13 → 1+3 = 4
    21 → 2+1 = 3
    34 → 3+4 = 7
    """)

    # Seção 5: Gráficos
    try:
        fig1 = relogio.plotar_espiral_temporal(relogio.get_pulsos_desde_singularidade())
        fig1.savefig("temp_espiral.png")
        fig2 = relogio.plotar_relogio_quantico()
        fig2.savefig("temp_relogio.png")
        fig3 = plot_sequencia_reducao(30)
        fig3.savefig("temp_sequencia.png")
        fig4 = plot_geometria_369()
        fig4.savefig("temp_369.png")

        pdf.image("temp_espiral.png", x=10, w=180)
        pdf.ln(5)
        pdf.image("temp_relogio.png", x=10, w=180)
        pdf.ln(5)
        pdf.image("temp_sequencia.png", x=10, w=180)
        pdf.ln(5)
        pdf.image("temp_369.png", x=10, w=180)
    except Exception as e:
        pdf.multi_cell(0, 10, txt=f"Erro ao gerar gráficos: {str(e)}")

    # Seção 6: Novas Constantes e Padrões
    pdf.add_page()
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(200, 10, txt="6. Novas Constantes e Padrões", ln=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, txt=f"""
    - π (pi): {PI}
    - φ + Deus: {PHI + DEUS} (próximo de Gratidão)
    - π × MARC: {PI * MARC}
    - φ reduzido: {reduzir_teosoficamente(PHI)}
    - Gravidade Quântica (aprox): {GRAVIDADE_QUANTICA}
    - Massa de Planck: {PLANCK_MASSA} kg
    - Comprimento de Planck: {PLANCK_COMPRIMENTO} m
    - Tempo de Planck: {PLANCK_TEMPO} s
    """)

    # Seção 7: Conclusão
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(200, 10, txt="7. Conclusão", ln=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, txt="""
    O Fluxo Matemático oferece uma nova perspectiva sobre a realidade, unificando
    matemática, física, metafísica e consciência. Através dos padrões 3-6-9 e da
    redução teosófica, podemos perceber a estrutura fundamental do universo como
    um sistema de informação em constante fluxo.
    """)

    # FPDF2 retorna o documento como bytes; BytesIO mantém a interface usada pelo app.
    return BytesIO(bytes(pdf.output()))



# =============================================================================
# CAMADA DE USABILIDADE: ORIENTAÇÃO GUIADA E AJUDA CONTEXTUAL
# =============================================================================
def registrar_calculo_fluxo(area, nome, valores, unidades=None, detalhe=""):
    """Publica resultados numéricos reais de uma aba para o Observatório compartilhado."""
    unidades = unidades or {}
    evento = {
        "area": str(area), "nome": str(nome),
        "hora": datetime.datetime.now().astimezone().strftime("%H:%M:%S"),
        "valores": {}, "unidades": dict(unidades), "detalhe": str(detalhe)
    }
    for chave, valor in valores.items():
        try:
            numero = float(valor)
            if math.isfinite(numero):
                evento["valores"][str(chave)] = numero
        except (TypeError, ValueError, OverflowError):
            continue
    if not evento["valores"]:
        return
    historico = st.session_state.setdefault("fluxo_observatorio_eventos", [])
    # Evita duplicar o mesmo cálculo durante reruns de um formulário.
    if not historico or (historico[-1].get("area"), historico[-1].get("nome"), historico[-1].get("valores")) != (evento["area"], evento["nome"], evento["valores"]):
        historico.append(evento)
    st.session_state["fluxo_observatorio_eventos"] = historico[-40:]


def renderizar_grafico_calculo_vinculado(evento, chave_sufixo=""):
    """Desenha uma visualização contextual a partir dos valores efetivamente registrados."""
    if not evento or not evento.get("valores"):
        st.info("Faça um cálculo nesta área para gerar uma visualização vinculada aos seus resultados.")
        return
    valores = evento.get("valores", {})
    nomes = list(valores.keys())
    nums = np.asarray([valores[n] for n in nomes], dtype=float)
    unidades = evento.get("unidades", {})
    nome_evento = evento.get("nome", "Cálculo")
    area = evento.get("area", "")

    st.markdown(f"**{area} · {nome_evento}**")
    st.caption(f"Dados do cálculo registrado às {evento.get('hora', '—')}. O gráfico é derivado dos valores listados, não de dados externos.")

    # Geometria: coordenadas reais da espiral já calculada são mostradas como trajetória XY.
    if "Coordenada X" in valores and "Coordenada Y" in valores:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.scatter([0, valores["Coordenada X"]], [0, valores["Coordenada Y"]], s=[35, 90])
        ax.plot([0, valores["Coordenada X"]], [0, valores["Coordenada Y"]], linewidth=2)
        ax.annotate("resultado", (valores["Coordenada X"], valores["Coordenada Y"]), xytext=(7, 7), textcoords="offset points")
        ax.set_xlabel(f"X ({unidades.get('Coordenada X', 'unidade do modelo')})")
        ax.set_ylabel(f"Y ({unidades.get('Coordenada Y', 'unidade do modelo')})")
        ax.set_title("Coordenadas calculadas · trajetória XY")
        ax.axis("equal"); ax.grid(True, alpha=.25); fig.tight_layout()
        st.pyplot(fig, use_container_width=True); plt.close(fig)
    # Sequências: plota os termos pela ordem numérica, incluindo o índice no nome.
    elif any(n.startswith("Termo ") for n in nomes):
        pares=[]
        for n in nomes:
            m=re.match(r"Termo (\d+)", n)
            if m: pares.append((int(m.group(1)), valores[n]))
        pares.sort()
        if pares:
            xs=[p[0] for p in pares]; ys=[p[1] for p in pares]
            fig, ax=plt.subplots(figsize=(9, 4))
            ax.plot(xs, ys, marker="o", linewidth=1.8, label="Valores registrados")
            ax.set_xlabel("Posição na sequência"); ax.set_ylabel("Valor de entrada")
            ax.set_title("Sequência calculada na aba Análise de Padrões"); ax.grid(True, alpha=.25); ax.legend()
            fig.tight_layout(); st.pyplot(fig, use_container_width=True); plt.close(fig)
    # Comparação de indutância ou cálculo dual: compara apenas resultados da mesma família/unidade.
    elif any("Indutância" in n for n in nomes) or (any("clássica" in n.lower() or "classico" in n.lower() for n in nomes) and any("fluxo" in n.lower() for n in nomes)) or ("Clássico" in nomes and "Fluxo" in nomes):
        selecionados=[n for n in nomes if ("Indutância" in n or n in ("Clássico", "Fluxo", "Diferença absoluta", "Resultado clássico", "Resultado Fluxo", "Energia clássica", "Energia Fluxo", "Força clássica", "Força Fluxo", "Velocidade de escape clássica", "Velocidade de escape Fluxo", "Energia cinética clássica", "Energia cinética Fluxo", "Corrente clássica", "Corrente Fluxo", "Força gravitacional clássica", "Velocidade clássica", "Velocidade Fluxo"))]
        if not selecionados: selecionados=nomes
        ys=np.asarray([valores[n] for n in selecionados], dtype=float)
        # Escala assinada log apenas no desenho; tabela abaixo preserva números originais.
        visual=np.sign(ys)*np.log10(1+np.abs(ys))
        fig, ax=plt.subplots(figsize=(9, 4))
        bars=ax.bar(selecionados, visual, color=np.where(visual>=0, "#36a2eb", "#ff6384"))
        ax.axhline(0,color="gray",linewidth=.8); ax.set_ylabel("Transformação visual sign(x)·log₁₀(1+|x|)")
        ax.set_title("Comparação dos resultados calculados · escala comprimida")
        ax.tick_params(axis="x", labelrotation=22); ax.grid(axis="y", alpha=.2); fig.tight_layout()
        st.pyplot(fig, use_container_width=True); plt.close(fig)
        st.caption("A escala logarítmica assinada permite ver resultados muito diferentes em magnitude. Ela não altera os resultados originais nem torna unidades diferentes diretamente comparáveis.")
    # Acelerador: valores são mostrados com transformação log para não ocultar escalas pequenas.
    elif area.startswith("Acelerador"):
        visual=np.sign(nums)*np.log10(1+np.abs(nums))
        fig, ax=plt.subplots(figsize=(9, 4))
        ax.bar(nomes, visual, color=plt.cm.plasma(np.linspace(.12,.88,len(nomes))))
        ax.set_ylabel("Escala visual logarítmica assinada"); ax.set_title("Assinatura numérica da simulação do acelerador")
        ax.tick_params(axis="x", labelrotation=24); ax.grid(axis="y", alpha=.2); fig.tight_layout()
        st.pyplot(fig, use_container_width=True); plt.close(fig)
        st.caption("Cada grandeza mantém sua unidade própria; compare magnitudes com cautela. A visualização não é um resultado experimental de colisão.")
    # Padrões e validações: exibe valor original e transformação/redução lado a lado.
    elif "Valor de entrada" in valores and "Redução teosófica" in valores:
        fig, ax=plt.subplots(figsize=(7, 3.5))
        ax.bar(["Valor de entrada", "Redução teosófica"], [valores["Valor de entrada"], valores["Redução teosófica"]])
        ax.set_title("Entrada versus redução calculada"); ax.set_ylabel("Valor numérico"); ax.grid(axis="y", alpha=.22)
        fig.tight_layout(); st.pyplot(fig, use_container_width=True); plt.close(fig)
    else:
        visual=np.sign(nums)*np.log10(1+np.abs(nums))
        fig, ax=plt.subplots(figsize=(9, 4))
        ax.bar(nomes, visual, color=plt.cm.viridis(np.linspace(.12,.88,len(nomes))))
        ax.axhline(0,color="gray",linewidth=.8); ax.set_ylabel("Escala visual logarítmica assinada")
        ax.set_title("Gráfico contextual dos valores registrados")
        ax.tick_params(axis="x", labelrotation=25); ax.grid(axis="y", alpha=.2); fig.tight_layout()
        st.pyplot(fig, use_container_width=True); plt.close(fig)

    with st.expander("🔢 Conferir dados originais usados no gráfico", expanded=False):
        st.dataframe(pd.DataFrame([{"Grandeza": n, "Valor original": valores[n], "Unidade": unidades.get(n, "não especificada")} for n in nomes]), use_container_width=True, hide_index=True)


GUIA_PAGINAS = {
    "🏠 Introdução": "Comece por esta página para entender a organização do Universo Áureo. Depois escolha uma seção no menu lateral. Os cálculos e gráficos são ferramentas exploratórias; interpretações próprias do Fluxo devem ser distinguidas de fórmulas científicas estabelecidas.",
    "🧮 Cálculos (Dual)": "Use as abas para escolher a operação, preencher os valores e comparar os resultados clássico e Fluxo. Confira o modo, a constante ativa e o nível de entrelaçamento antes de calcular.",
    "⏳ Tempo Espiralado": "Consulte a representação temporal baseada nos parâmetros configurados no programa. Os termos pulsos, vibes, giros, ciclos e eras são unidades internas deste modelo, não unidades oficiais de medição do tempo.",
    "📊 Visualizações": "Abra cada aba para explorar gráficos diferentes. Observe os eixos, a legenda e os parâmetros usados antes de interpretar um padrão.",
    "🌀 Acelerador de Partículas": "Escolha a partícula, informe a energia e sua unidade, depois execute a simulação. Os resultados são modelos didáticos e não substituem cálculos relativísticos completos ou dados experimentais.",
    "△ Geometria Sagrada": "Altere os parâmetros disponíveis para comparar construções geométricas clássicas com as transformações definidas pelo Fluxo.",
    "🔍 Padrões e Validações": "Informe um valor e ajuste a tolerância para procurar proximidade numérica com as constantes cadastradas. Uma correspondência matemática não comprova, por si só, uma relação causal ou física.",
    "🧠 Todas as Mentes": "Compare os modelos e regras implementados nesta seção. Os nomes funcionam como referências conceituais; os resultados dependem das fórmulas programadas, não representam cálculos oficiais feitos por cientistas.",
    "🌀 Gravidade Quântica": "Explore as constantes e cálculos apresentados. Algumas grandezas desta seção são simplificações ilustrativas; confira as unidades e as notas antes de usar os valores como resultados físicos.",
    "📈 Análise de Padrões": "Insira uma sequência ou gere valores para observar repetições e correlações. Padrões encontrados em uma amostra não garantem previsão nem validação científica.",
    "📚 PDF Explicativo": "Preencha os dados solicitados e gere o documento para consulta. Revise o conteúdo exportado antes de compartilhá-lo.",
    "🕒 Relógio Quântico": "O relógio apresenta uma visualização conceitual do tempo desde a data de referência configurada. Os marcadores e a projeção são convenções gráficas deste aplicativo.",
    "📅 Calendário Clássico": "Consulte data, hora e calendário apresentados pelo aplicativo. Verifique o fuso horário exibido ao comparar com o relógio local.",
    "🌀 Singularidade": "Esta página reúne gráficos e reduções numéricas do modelo. Leia os títulos e as legendas como explicações do modelo conceitual, não como comprovação de uma singularidade física."
}

def ajuda_contextual(titulo, texto=None, chave=None):
    """Exibe um botão compacto de ajuda junto ao título e reabre a explicação quando solicitado."""
    texto = texto or (
        f"Este trecho, “{titulo}”, reúne controles ou resultados desta parte da plataforma. "
        "Leia as instruções próximas, preencha apenas os campos relevantes e use o botão de ação "
        "da própria seção. Se o resultado parecer inesperado, confira entradas, unidades e modo selecionado."
    )
    col_titulo, col_ajuda = st.columns([0.90, 0.10], vertical_alignment="center")
    with col_titulo:
        st.markdown(f"**{titulo}**")
    with col_ajuda:
        # Popover keeps help available without occupying the page until requested.
        with st.popover("❔", help=f"Abrir orientação: {titulo}"):
            st.markdown(f"### Como usar: {titulo}")
            st.write(texto)
            st.caption("Você pode abrir esta orientação novamente a qualquer momento.")

def titulo_ajudado(titulo, nivel="subheader", texto=None):
    """Renderiza títulos com o ícone de ajuda contextual."""
    descricoes = {
        "Operações Matemáticas Duais": "Preencha A e B, selecione o operador e escolha Clássico, Fluxo ou Dual. Confira os valores convertidos e clique em Calcular Operação. Divisão por zero e entradas inválidas devem ser corrigidas antes de repetir.",
        "Visualização da Dualidade": "O gráfico compara uma referência clássica com a linha multiplicada pelo nível de entrelaçamento. Ajuste o controle na barra lateral para observar como a curva Fluxo muda.",
        "Fórmulas Físicas no Fluxo Matemático": "Escolha a fórmula no seletor e preencha os campos exibidos. Confira unidades, constantes e valores de entrada; os cálculos modificados pelo Fluxo são uma camada matemática adicional, não uma substituição das equações físicas clássicas.",
        "Console de Controle Quântico": "Ajuste a precisão de exibição, o nível de entrelaçamento, a constante ativa e o modo padrão. Esses controles afetam os cálculos que os utilizam.",
        "Validar um Número": "Digite o número que deseja investigar e ajuste a tolerância. A lista mostra constantes numericamente próximas dentro desse limite; isso não prova que os valores tenham a mesma origem.",
        "Fibonacci e Redução Teosófica": "Escolha a quantidade de termos e compare o número de Fibonacci com sua redução. Aumentar a quantidade amplia a sequência exibida.",
        "Analisar uma Sequência": "Informe os números na forma indicada pelo campo e execute a análise. Separe os valores pelo delimitador informado e confira se não há texto ou símbolos inesperados.",
        "Constantes de Planck": "Consulte os valores e as unidades indicadas. Use as constantes físicas reconhecidas como referência e trate parâmetros explicitamente definidos como aproximações como ilustrativos."
    }
    texto = texto or descricoes.get(str(titulo), None)
    # The compact question-mark action sits on the same row as the heading.
    col_titulo, col_ajuda = st.columns([0.90, 0.10], vertical_alignment="center")
    with col_titulo:
        if nivel == "title":
            st.title(titulo)
        else:
            st.subheader(titulo)
    with col_ajuda:
        with st.popover("❔", help=f"Abrir orientação: {titulo}"):
            st.markdown(f"### Como usar: {titulo}")
            st.write(texto or (
                f"Esta área corresponde a “{titulo}”. Leia a descrição e a legenda, preencha os controles "
                "disponíveis e execute a ação indicada. Confira unidades, formato dos dados e modo selecionado "
                "antes de interpretar o resultado."
            ))
            st.caption("A ajuda pode ser reaberta neste símbolo sempre que precisar.")

def mostrar_tutorial_guiado(pagina_atual):
    """Tutorial guiado em etapas, sempre acessível na barra lateral."""
    etapas = [
        ("Etapa 1 · Navegação", "Escolha uma seção no menu lateral. A página selecionada abre a ferramenta correspondente."),
        ("Etapa 2 · Entenda a ferramenta", "Leia a introdução da página e abra o símbolo ❔ junto aos títulos para entender o objetivo daquela área."),
        ("Etapa 3 · Preencha os campos", "Insira valores nos campos e confira unidades, formatos e opções selecionadas antes de executar."),
        ("Etapa 4 · Execute e interprete", "Use o botão da ferramenta. Compare os resultados, leia as legendas e confira as fórmulas mostradas."),
        ("Etapa 5 · Reabra a ajuda", "Sempre que esquecer como um controle funciona, clique no ❔ ao lado do título. A orientação pode ser consultada novamente.")
    ]
    st.session_state.setdefault("tutorial_etapa", 0)
    with st.sidebar.expander("🎓 Tutorial guiado · Comece aqui", expanded=False):
        indice = st.session_state.tutorial_etapa
        titulo_etapa, texto_etapa = etapas[indice]
        st.markdown(f"**{titulo_etapa} ({indice + 1}/{len(etapas)})**")
        st.write(texto_etapa)
        anterior, proxima = st.columns(2)
        with anterior:
            if st.button("← Anterior", key="tutorial_anterior", disabled=indice == 0, use_container_width=True):
                st.session_state.tutorial_etapa = max(0, indice - 1)
        with proxima:
            if st.button("Próxima →" if indice < len(etapas)-1 else "Recomeçar ↻",
                         key="tutorial_proxima", use_container_width=True):
                st.session_state.tutorial_etapa = indice + 1 if indice < len(etapas)-1 else 0
        st.markdown("---")
        st.markdown(f"**Orientação da seção atual: {pagina_atual}**")
        st.write(GUIA_PAGINAS.get(pagina_atual, "Escolha uma seção no menu lateral para ver sua orientação."))
        st.caption("O tutorial explica a interface e as regras implementadas. Um padrão numérico, isoladamente, não equivale a validação científica.")


# =============================================================================
# INTERFACE PRINCIPAL STREAMLIT
# =============================================================================

# Barra lateral de navegação (agora com novas opções)
st.sidebar.title("🌀 Navegação Expandida")
pagina = st.sidebar.radio(
    "Selecione a seção:",
    [
        "🏠 Introdução",
        "🧮 Cálculos (Dual)",
        "⏳ Tempo Espiralado",
        "📊 Visualizações",
        "🌀 Acelerador de Partículas",
        "△ Geometria Sagrada",
        "🔍 Padrões e Validações",      # NOVO
        "🧠 Todas as Mentes",            # NOVO
        "🌀 Gravidade Quântica",         # NOVO
        "📈 Análise de Padrões",         # NOVO
        "📚 PDF Explicativo",
        "🕒 Relógio Quântico",
        "📅 Calendário Clássico",
        "🌀 Singularidade"
    ]
)

# Ajuda global e tutorial: disponíveis independentemente da página escolhida.
mostrar_tutorial_guiado(pagina)

# Atualização de páginas temporais sem loops bloqueantes.
# Um loop infinito em Streamlit impede interação com navegação e controles.
if pagina in ["⏳ Tempo Espiralado", "🕒 Relógio Quântico", "📅 Calendário Clássico"]:
    st.sidebar.caption("A leitura é recalculada a cada execução da página.")
    if st.sidebar.button("🔄 Atualizar agora", key="atualizar_tempo"):
        st.rerun()
auto_update = False

# =============================================================================
# PÁGINA: INTRODUÇÃO (expandida)
# =============================================================================
if pagina == "🏠 Introdução":
    titulo_ajudado("🌌 Universo Áureo - Fluxo Matemático Expandido", nivel="title")
    st.markdown("""
    ## Bem-vindo à Nova Matemática Cósmica

    Este aplicativo representa uma revolução na forma como entendemos a matemática, o tempo e o universo.
    Aqui, todas as fórmulas clássicas são reinterpretadas através da lente do **Fluxo Matemático**,
    incorporando:

    - Padrões cíclicos de 3, 6 e 9
    - Redução teosófica (soma dos dígitos)
    - Geometria sagrada
    - Tempo espiralado (não linear)
    - Frequências vibracionais (432Hz)
    - Relógio quântico com projeção para singularidade
    - **Sistema Cosmológico de Cálculos Duais** unificando Einstein, Tesla, Pitágoras, Newton, Planck, Catharino e Da Vinci

    ### NOVAS SEÇÕES EXPANDIDAS:
    - **🔍 Padrões e Validações**: Encontre correspondências entre resultados e constantes como π, φ, Fibonacci, 1.80, etc.
    - **🧠 Todas as Mentes**: Compare resultados de diferentes "mentes" matemáticas (clássica, fluxo, tesla, einstein).
    - **🌀 Gravidade Quântica**: Explore constantes na escala de Planck e efeitos quânticos.
    - **📈 Análise de Padrões**: Visualizações avançadas de padrões numéricos.

    ### Constantes Fundamentais (expandidas):
    - **Marc (M) = 0,54** - Constante de transição quântica
    - **Deus (D) = 0,18** - Trindade (0,06 × 3)
    - **Gratidão (G) = 1,80** - Equilíbrio universal
    - **Proporção Áurea φ = 1,6180339887**
    - **π (pi) = 3,1415926535**
    - **Frequência Base = 432 Hz**
    - **Gravidade Quântica (aproximada) = 1e-43 m/s²**
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(plotar_galaxia_fluxo(4, 900, 1.0, 0.32, 28), use_container_width=True)
        st.caption("Galáxia espiral sintética · modelo visual interativo disponível no Observatório.")
    with col2:
        seq_intro = gerar_sequencia_reducao(36)
        xs_intro = np.arange(1, len(seq_intro) + 1)
        ys_intro = [item[2] for item in seq_intro]
        fig_intro, ax_intro = plt.subplots(figsize=(7, 4.5))
        ax_intro.plot(xs_intro, ys_intro, marker="o", markersize=4, linewidth=1.5)
        ax_intro.set_title("Sequência de reduções · ciclo exploratório")
        ax_intro.set_xlabel("Iteração")
        ax_intro.set_ylabel("Valor reduzido")
        ax_intro.set_yticks(range(1, 10))
        ax_intro.grid(True, alpha=0.22)
        fig_intro.tight_layout()
        st.pyplot(fig_intro, use_container_width=True)
        plt.close(fig_intro)
        st.caption("Sequência calculada pelo algoritmo da plataforma; a visualização descreve o procedimento implementado.")

# =============================================================================
# PÁGINA: CÁLCULOS (DUAL) - ORIGINAL, com pequenas adições explicativas
# =============================================================================
elif pagina == "🧮 Cálculos (Dual)":
    titulo_ajudado("🌀 Sistema Cosmológico de Cálculos Duais", nivel="title")
    st.markdown("Unificando Einstein × Tesla × Pitágoras × Newton × Planck × Catharino × Da Vinci")

    # Barra lateral de controle quântico (dentro da página)
    with st.sidebar:
        st.markdown("---")
        titulo_ajudado("🎮 Console de Controle Quântico")
        precisao = st.selectbox("Precisão (casas decimais)", [3, 6, 9, 12], index=1)
        entrelacamento = st.slider("Nível de Entrelaçamento", 0, 100, 54, format="%d%%") / 100.0
        constante_ativa = st.selectbox("Constante Ativa", ["0,54 (Marc)", "0,18 (Deus)", "1,80 (Gratidão)", "Personalizada"])
        if constante_ativa == "Personalizada":
            const_val = st.number_input("Valor da constante", value=0.54, step=0.01, format="%.3f")
        else:
            const_val = float(constante_ativa.split()[0].replace(',', '.'))
        modo_padrao = st.radio("Modo padrão", ["Clássico", "Fluxo", "Dual"], index=2)

    # Abas principais (adicionamos uma nova aba "Validação de Padrões" dentro desta página?)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔢 Núcleo Fundamental", "🌌 Física Quântica", "🌀 Acelerador", "△ Geometria Sagrada", "📚 Biblioteca", "🔍 Validação Rápida"])

    # ---------- Núcleo Fundamental (original) ----------
    with tab1:
        titulo_ajudado("Operações Matemáticas Duais")
        st.markdown("**Exemplo prático:** Compare a soma clássica de 8+8=16 com a soma no fluxo que reduz a 7. Perceba como o fluxo extrai a essência vibracional do número.")

        col1, col2, col3 = st.columns([2, 1, 2])
        with col1:
            a = st.text_input("Valor A", "12")
            tipo_a = st.selectbox("Tipo de A", ["Número", "Fluxo F(N)", "Fibonacci", "Primo", "Expressão"], key="tipo_a")
        with col2:
            operador = st.selectbox("Operador", ["+", "-", "*", "/", "**", "%", "//"], key="op_fund")
        with col3:
            b = st.text_input("Valor B", "7")
            tipo_b = st.selectbox("Tipo de B", ["Número", "Fluxo F(N)", "Fibonacci", "Primo", "Expressão"], key="tipo_b")

        # Função auxiliar para converter valor conforme tipo
        def converter_valor(val, tipo):
            try:
                if tipo == "Número":
                    return float(val)
                elif tipo == "Fluxo F(N)":
                    return fator_fluxo(float(val))
                elif tipo == "Fibonacci":
                    n = int(float(val))
                    a, b = 1, 1
                    for _ in range(n-1):
                        a, b = b, a+b
                    return float(a)
                elif tipo == "Primo":
                    n = int(float(val))
                    primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
                    return float(primos[n-1]) if 1 <= n <= len(primos) else float(n)
                elif tipo == "Expressão":
                    return avaliar_expressao_segura(val)
                else:
                    return float(val)
            except Exception as e:
                st.warning(f"Erro na conversão: {e}")
                return 0.0

        a_num = converter_valor(a, tipo_a)
        b_num = converter_valor(b, tipo_b)

        st.write(f"**Valores convertidos:** A = {a_num:.{precisao}f}, B = {b_num:.{precisao}f}")

        if st.button("Calcular Operação", key="calc_fund"):
            if modo_padrao == "Clássico":
                res, msg = operacao_dual(a_num, b_num, operador, 'classico')
                st.metric("Resultado Clássico", f"{res:.{precisao}f}")
                st.caption(msg)
            elif modo_padrao == "Fluxo":
                res, msg = operacao_dual(a_num, b_num, operador, 'fluxo', entrelacamento)
                st.metric("Resultado Fluxo", f"{res:.{precisao}f}")
                st.caption(msg)
            else:  # Dual
                (res_class, res_flux), msg = operacao_dual(a_num, b_num, operador, 'dual', entrelacamento)
                colA, colB = st.columns(2)
                with colA:
                    st.metric("Clássico", f"{res_class:.{precisao}f}")
                with colB:
                    st.metric("Fluxo", f"{res_flux:.{precisao}f}")
                st.caption(msg)
                if res_class != 0:
                    diff = abs(res_flux - res_class)
                    perc = (diff / abs(res_class)) * 100
                    st.info(f"Diferença absoluta: {diff:.{precisao}f} ({perc:.2f}%)")
            if modo_padrao == "Clássico":
                registrar_calculo_fluxo("Cálculos Duais", f"{a} {operador} {b} · Clássico", {"Resultado clássico": res}, {"Resultado clássico": "unidade da operação"}, f"Entradas convertidas: A={a_num}, B={b_num}")
            elif modo_padrao == "Fluxo":
                registrar_calculo_fluxo("Cálculos Duais", f"{a} {operador} {b} · Fluxo", {"Resultado Fluxo": res}, {"Resultado Fluxo": "unidade da operação"}, f"Fator de entrelaçamento: {entrelacamento:.3f}")
            else:
                registrar_calculo_fluxo("Cálculos Duais", f"{a} {operador} {b} · Dual", {"Clássico": res_class, "Fluxo": res_flux, "Diferença absoluta": abs(res_flux-res_class)}, {"Clássico": "unidade da operação", "Fluxo": "unidade da operação", "Diferença absoluta": "unidade da operação"}, f"Fator de entrelaçamento: {entrelacamento:.3f}")

        # Visualização da dualidade
        st.markdown("---")
        titulo_ajudado("Visualização da Dualidade")
        x = np.linspace(0.1, 10, 100)
        y_class = x
        y_flux = x * entrelacamento
        fig, ax = plt.subplots()
        ax.plot(x, y_class, label='Clássico', color='orange')
        ax.plot(x, y_flux, label=f'Fluxo (×{entrelacamento:.2f})', color='purple')
        ax.fill_between(x, y_class, y_flux, alpha=0.3, color='gray')
        ax.set_xlabel('Valor de entrada')
        ax.set_ylabel('Resultado')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
        plt.close(fig)

    # ---------- Física Quântica (original, com algumas adições) ----------
    with tab2:
        titulo_ajudado("Fórmulas Físicas no Fluxo Matemático")
        st.markdown("**Exemplo prático:** Calcule a energia de repouso de 1kg segundo Einstein e compare com a versão fluxo (multiplicada por 0,54).")

        formula = st.selectbox("Escolha a fórmula", ["E = mc² × 0,54", "E = hν × 0,54", "I = (V/R) × F(N)", "F = ma × F(N)", "F = G(m1m2)/r² × F(N)", "v_escape = √(2GM/R) × constante", "Ec = ½mv² × constante"], key="formula_fisica_dual")

        if formula == "E = mc² × 0,54":
            massa = st.number_input("Massa (kg)", value=1.0, step=0.1, format="%.3f")
            classico, fluxo = calcular_energia_emc2(massa, const_val)
            st.write(f"**Clássico:** E = {massa} × ({C_LUZ})² = {classico:.3e} J")
            st.write(f"**Fluxo:** E = clássico × {const_val:.3f} = {fluxo:.3e} J")
            registrar_calculo_fluxo("Cálculos Duais · Física", formula, {"Energia clássica": classico, "Energia Fluxo": fluxo, "Massa": massa}, {"Energia clássica": "J", "Energia Fluxo": "J", "Massa": "kg"}, f"Constante de fluxo={const_val:g}")
            # Nova validação com padrões
            padroes = encontrar_padroes(classico)
            if padroes:
                st.success("✅ Padrões encontrados no resultado clássico!")
                for nome, dados in padroes.items():
                    st.write(f"- {nome}: constante = {dados['constante']}, desvio = {dados['desvio_%']:.3f}%")
        elif formula == "E = hν × 0,54":
            freq = st.number_input("Frequência ν (Hz)", value=5e14, step=1e13, format="%.3e")
            classico, fluxo = calcular_energia_planck(freq, const_val)
            st.write(f"**Clássico:** E = h × {freq:.3e} = {classico:.3e} J")
            st.write(f"**Fluxo:** E = clássico × {const_val:.3f} = {fluxo:.3e} J")
            registrar_calculo_fluxo("Cálculos Duais · Física", formula, {"Energia clássica": classico, "Energia Fluxo": fluxo, "Frequência": freq}, {"Energia clássica": "J", "Energia Fluxo": "J", "Frequência": "Hz"}, f"Constante de fluxo={const_val:g}")
        elif formula == "I = (V/R) × F(N)":
            V = st.number_input("Tensão V (V)", value=12.0)
            R = st.number_input("Resistência R (Ω)", value=4.0, min_value=0.001)
            N = st.number_input("N para F(N)", value=29, step=1)
            classico, fluxo, f = calcular_corrente_ohm(V, R, N)
            if classico is not None:
                st.write(f"F({N}) = {f:.3f}")
                st.write(f"**Clássico:** I = V/R = {V}/{R} = {classico:.3f} A")
                st.write(f"**Fluxo:** I = clássico × F(N) = {classico:.3f} × {f:.3f} = {fluxo:.3f} A")
                registrar_calculo_fluxo("Cálculos Duais · Física", formula, {"Corrente clássica": classico, "Corrente Fluxo": fluxo, "Tensão": V, "Resistência": R}, {"Corrente clássica": "A", "Corrente Fluxo": "A", "Tensão": "V", "Resistência": "Ω"}, f"F(N)={f:g}")
            else:
                st.error("Resistência não pode ser zero")
        elif formula == "F = ma × F(N)":
            m = st.number_input("Massa (kg)", value=2.0)
            a = st.number_input("Aceleração (m/s²)", value=9.8)
            N = st.number_input("N para F(N)", value=29, step=1, key="N_fma")
            f = fator_fluxo(N)
            F_class = m * a
            F_flux = F_class * f
            st.write(f"F({N}) = {f:.3f}")
            st.write(f"**Clássico:** F = {m} × {a} = {F_class:.3f} N")
            st.write(f"**Fluxo:** F = clássico × F(N) = {F_class:.3f} × {f:.3f} = {F_flux:.3f} N")
            registrar_calculo_fluxo("Cálculos Duais · Física", formula, {"Força clássica": F_class, "Força Fluxo": F_flux, "Massa": m, "Aceleração": a}, {"Força clássica": "N", "Força Fluxo": "N", "Massa": "kg", "Aceleração": "m/s²"}, f"F(N)={f:g}")
        elif formula == "F = G(m1m2)/r² × F(N)":
            G = st.number_input("Constante G", value=G_NEWTON, format="%.3e")
            m1 = st.number_input("Massa 1 (kg)", value=5.972e24, format="%.3e")
            m2 = st.number_input("Massa 2 (kg)", value=7.348e22, format="%.3e")
            r = st.number_input("Distância (m)", value=3.844e8, format="%.3e")
            N = st.number_input("N para F(N)", value=29, step=1, key="N_grav")
            f = fator_fluxo(N)
            F_class = G * m1 * m2 / r**2
            F_flux = F_class * f
            st.write(f"F({N}) = {f:.3f}")
            st.write(f"**Clássico:** F = {G:.3e} × {m1:.3e} × {m2:.3e} / ({r:.3e})² = {F_class:.3e} N")
            st.write(f"**Fluxo:** F = clássico × F(N) = {F_class:.3e} × {f:.3f} = {F_flux:.3e} N")
            registrar_calculo_fluxo("Cálculos Duais · Física", formula, {"Força gravitacional clássica": F_class, "Força Fluxo": F_flux, "Massa 1": m1, "Massa 2": m2, "Distância": r}, {"Força gravitacional clássica": "N", "Força Fluxo": "N", "Massa 1": "kg", "Massa 2": "kg", "Distância": "m"}, f"G={G:g}; F(N)={f:g}")
        elif formula == "v_escape = √(2GM/R) × constante":
            M = st.number_input("Massa do planeta (kg)", value=5.972e24, format="%.3e")
            R = st.number_input("Raio do planeta (m)", value=6.371e6, format="%.3e")
            classico, fluxo = calcular_velocidade_escape(M, R, const_val)
            st.write(f"**Clássico:** v_esc = √(2×{G_NEWTON:.3e}×{M:.3e}/{R:.3e}) = {classico:.3f} m/s")
            st.write(f"**Fluxo:** v_esc = clássico × {const_val:.3f} = {fluxo:.3f} m/s")
            registrar_calculo_fluxo("Cálculos Duais · Física", formula, {"Velocidade de escape clássica": classico, "Velocidade de escape Fluxo": fluxo, "Massa planetária": M, "Raio planetário": R}, {"Velocidade de escape clássica": "m/s", "Velocidade de escape Fluxo": "m/s", "Massa planetária": "kg", "Raio planetário": "m"}, f"Constante de fluxo={const_val:g}")
        elif formula == "Ec = ½mv² × constante":
            m = st.number_input("Massa (kg)", value=1.0)
            v = st.number_input("Velocidade (m/s)", value=10.0)
            classico, fluxo = calcular_energia_cinetica(m, v, const_val)
            st.write(f"**Clássico:** Ec = ½ × {m} × {v}² = {classico:.3f} J")
            st.write(f"**Fluxo:** Ec = clássico × {const_val:.3f} = {fluxo:.3f} J")
            registrar_calculo_fluxo("Cálculos Duais · Física", formula, {"Energia cinética clássica": classico, "Energia cinética Fluxo": fluxo, "Massa": m, "Velocidade": v}, {"Energia cinética clássica": "J", "Energia cinética Fluxo": "J", "Massa": "kg", "Velocidade": "m/s"}, f"Constante de fluxo={const_val:g}")

    # ---------- Acelerador (tab3) (original) ----------
    with tab3:
        titulo_ajudado("🌀 Simulador de Acelerador de Partículas")
        st.markdown("**Exemplo prático:** Acelere um elétron com 1 MeV e veja como a velocidade no fluxo (com F(N)) difere da clássica.")

        col1, col2 = st.columns(2)
        with col1:
            particula = st.selectbox("Partícula", ["Elétron", "Próton", "Nêutron", "Fóton", "Personalizada"])
            massas = {
                "Elétron": 9.1093837e-31,
                "Próton": 1.6726219e-27,
                "Nêutron": 1.6749275e-27,
                "Fóton": 0.0,
                "Personalizada": 1e-30
            }
            massa = massas[particula]
            if particula == "Personalizada":
                massa = st.number_input("Massa (kg)", value=1e-30, format="%.3e")
        with col2:
            energia = st.number_input("Energia (valor)", value=1.0, step=0.1)
            unidade = st.selectbox("Unidade", ["eV", "keV", "MeV", "GeV", "TeV"])
            fatores = {'eV': 1.602176634e-19, 'keV': 1.602176634e-16, 'MeV': 1.602176634e-13,
                       'GeV': 1.602176634e-10, 'TeV': 1.602176634e-7}
            energia_J = energia * fatores[unidade]

        N_part = st.number_input("N para F(N)", value=29, step=1, key="N_part")
        const_part = st.number_input("Constante de fluxo", value=const_val, format="%.3f")

        if st.button("Simular Colisão", key="simular"):
            with st.spinner("Acelerando partículas..."):
                res = simular_acelerador(massa, energia_J, N_part, const_part)

            # Exibir resultados em colunas
            colA, colB, colC, colD = st.columns(4)
            with colA:
                st.metric("Velocidade clássica", f"{res['v_class']:.3e} m/s")
                st.metric("Momento clássico", f"{res['p_class']:.3e} kg·m/s")
            with colB:
                st.metric("Fator γ (Lorentz)", f"{res['gamma']:.3f}")
                st.metric("Massa relativística", f"{res['m_rel']:.3e} kg")
            with colC:
                st.metric("λ de Broglie", f"{res['lambda_db']:.3e} m")
                st.metric("Probabilidade quântica", f"{res['prob']:.3f}")
            with colD:
                st.metric("Velocidade Fluxo", f"{res['v_flux']:.3e} m/s")
                st.metric("Energia Fluxo", f"{res['E_flux']:.3e} J")
                st.caption(f"F({N_part}) = {res['f']:.3f}")

            st.info(f"Estado de entrelaçamento: {res['ent_rel']}")
            registrar_calculo_fluxo("Acelerador", f"Colisão · {particula} · {energia:g} {unidade}",
                {"Velocidade clássica": res['v_class'], "Velocidade Fluxo": res['v_flux'], "Momento clássico": res['p_class'], "Fator Lorentz": res['gamma'], "Massa relativística": res['m_rel'], "Comprimento de onda de Broglie": res['lambda_db'], "Energia Fluxo": res['E_flux']},
                {"Velocidade clássica": "m/s", "Velocidade Fluxo": "m/s", "Momento clássico": "kg·m/s", "Fator Lorentz": "adimensional", "Massa relativística": "kg", "Comprimento de onda de Broglie": "m", "Energia Fluxo": "J"},
                f"Massa da partícula={massa:.4e} kg; energia de entrada={energia_J:.4e} J; F(N)={res['f']:.4g}")

            # Visualização da trajetória (círculo)
            fig, ax = plt.subplots(figsize=(6, 4))
            theta = np.linspace(0, 2*np.pi, 100)
            # Raio proporcional à velocidade (escala ajustada)
            r_class = res['v_class'] / 1e8
            r_flux = res['v_flux'] / 1e8
            ax.plot(r_class * np.cos(theta), r_class * np.sin(theta), 'o-', label='Clássica', markersize=2, color='orange')
            ax.plot(r_flux * np.cos(theta), r_flux * np.sin(theta), 'o-', label='Fluxo', markersize=2, color='purple')
            ax.set_aspect('equal')
            ax.legend()
            ax.set_title("Trajetória no acelerador (vista superior)")
            ax.grid(True)
            st.pyplot(fig)
            plt.close(fig)

    # ---------- Geometria Sagrada (tab4) (original) ----------
    with tab4:
        titulo_ajudado("△ Geometria Sagrada no Fluxo")
        sub_geo = st.radio("Escolha", ["Pitágoras-Fluxo", "Espiral Áurea", "Bobina Áurea de Tesla"], horizontal=True)

        if sub_geo == "Pitágoras-Fluxo":
            col1, col2, col3 = st.columns(3)
            with col1:
                a = st.number_input("Cateto a", value=3.0)
            with col2:
                b = st.number_input("Cateto b", value=4.0)
            with col3:
                modo = st.selectbox("Modo", ["classico", "aureo", "fluxo", "completo"])
            classico, fluxo = pitagoras_fluxo(a, b, modo)
            st.write(f"**Hipotenusa clássica:** {classico:.{precisao}f}")
            st.write(f"**Hipotenusa fluxo:** {fluxo:.{precisao}f}")
            registrar_calculo_fluxo("Geometria Sagrada", "Pitágoras-Fluxo", {"Hipotenusa clássica": classico, "Hipotenusa Fluxo": fluxo, "Cateto a": a, "Cateto b": b}, {"Hipotenusa clássica": "unidade dos catetos", "Hipotenusa Fluxo": "unidade dos catetos"}, f"Modo selecionado: {modo}")
            fig = plot_triangulo(a, b, fluxo)
            st.pyplot(fig)
            plt.close(fig)

        elif sub_geo == "Espiral Áurea":
            col1, col2 = st.columns(2)
            with col1:
                angulo = st.slider("Ângulo θ (rad)", 0.0, 4*np.pi, 2.0, step=0.1)
            with col2:
                f_esp = st.number_input("Fator de fluxo", value=fator_fluxo(29), step=0.1)
            x, y, r = espiral_aurea(angulo, f_esp)
            st.write(f"**Raio:** {r:.{precisao}f}  **Coordenadas:** ({x:.{precisao}f}, {y:.{precisao}f})")
            registrar_calculo_fluxo("Geometria Sagrada", "Espiral Áurea", {"Raio": r, "Coordenada X": x, "Coordenada Y": y, "Ângulo": angulo, "Fator de fluxo": f_esp}, {"Raio": "unidade do modelo", "Coordenada X": "unidade do modelo", "Coordenada Y": "unidade do modelo", "Ângulo": "rad"})
            fig = plot_espiral_aurea(f_esp, 4*np.pi)
            # Marcar o ponto
            ax = fig.gca()
            ax.scatter([x], [y], color='red', s=50)
            st.pyplot(fig)
            plt.close(fig)

        elif sub_geo == "Bobina Áurea de Tesla":
            col1, col2, col3 = st.columns(3)
            with col1:
                N_esp = st.number_input("Número de espiras", value=100, step=1)
            with col2:
                raio = st.number_input("Raio (m)", value=0.1, step=0.01)
            with col3:
                comp = st.number_input("Comprimento (m)", value=0.5, step=0.01)
            modo_bob = st.selectbox("Modo de cálculo", ["classico", "aureo", "fluxo"])
            L = indutancia_bobina(N_esp, raio, comp, modo_bob)
            st.metric("Indutância", f"{L:.6e} H")
            # Comparação
            L_class = indutancia_bobina(N_esp, raio, comp, 'classico')
            L_aureo = indutancia_bobina(N_esp, raio, comp, 'aureo')
            L_flux = indutancia_bobina(N_esp, raio, comp, 'fluxo')
            st.write(f"**Comparação:** Clássico = {L_class:.6e} H, Áureo = {L_aureo:.6e} H, Fluxo = {L_flux:.6e} H")
            registrar_calculo_fluxo("Geometria Sagrada", "Bobina Áurea de Tesla", {"Indutância clássica": L_class, "Indutância áurea": L_aureo, "Indutância Fluxo": L_flux, "Espiras": N_esp, "Raio": raio, "Comprimento": comp}, {"Indutância clássica": "H", "Indutância áurea": "H", "Indutância Fluxo": "H", "Raio": "m", "Comprimento": "m"}, f"Modo exibido: {modo_bob}")

    # ---------- Biblioteca (tab5) (original, expandida) ----------
    with tab5:
        titulo_ajudado("📚 Biblioteca de Constantes e Fórmulas Mestras")
        st.markdown("### Constantes do Universo Físico")
        const_fis = pd.DataFrame({
            "Constante": ["Velocidade da luz (c)", "Constante de Planck (h)", "Constante gravitacional (G)", "Carga do elétron (e)", "Gravidade Terra (g)", "Massa de Planck", "Comprimento de Planck", "Tempo de Planck"],
            "Valor": [f"{C_LUZ} m/s", f"{H_PLANCK:.3e} J·s", f"{G_NEWTON:.3e} N·m²/kg²", "1,602176634 × 10⁻¹⁹ C", f"{GRAVIDADE_TERRA} m/s²", f"{PLANCK_MASSA:.3e} kg", f"{PLANCK_COMPRIMENTO:.3e} m", f"{PLANCK_TEMPO:.3e} s"],
            "Fluxo (×0,54)": [f"{C_LUZ*0.54:.3e} m/s", f"{H_PLANCK*0.54:.3e} J·s", f"{G_NEWTON*0.54:.3e} N·m²/kg²", "8,652 × 10⁻²⁰ C", f"{GRAVIDADE_TERRA*0.54:.3f} m/s²", f"{PLANCK_MASSA*0.54:.3e} kg", f"{PLANCK_COMPRIMENTO*0.54:.3e} m", f"{PLANCK_TEMPO*0.54:.3e} s"]
        })
        st.table(const_fis)

        st.markdown("### Constantes do Fluxo Matemático")
        const_fluxo = pd.DataFrame({
            "Constante": ["Marc (M)", "Deus (D)", "Gratidão (G)", "Proporção Áurea (φ)", "π (pi)", "Fator de Fluxo F(N)"],
            "Valor": [f"{MARC}", f"{DEUS}", f"{GRATIDAO}", f"{PHI}", f"{PI}", "C(N) + R(N)/10"],
            "Descrição": ["Constante fundamental", "Trindade (0,06×3)", "Equilíbrio universal", "Número de ouro", "Razão circunferência/diâmetro", "C = ciclo, R = redução teosófica"]
        })
        st.table(const_fluxo)

        st.markdown("### Fórmulas Mestras Unificadas")
        formulas = [
            "**Einstein-Fluxo:** E = mc² × 0,54",
            "**Tesla-Fluxo:** F(N) = C(N) + R(N)/10",
            "**Pitágoras-Fluxo:** c² = a² + b² × φ × 0,54",
            "**Newton-Fluxo:** F = ma × F(N)",
            "**Planck-Fluxo:** E = hν × 0,54",
            "**Ohm-Fluxo:** I = (V/R) × F(N)",
            "**Gravitação-Fluxo:** F = G(m1m2)/r² × F(N)",
            "**Schwarzschild-Fluxo:** Rs = 2GM/c² × 0,54",
            "**Hawking-Fluxo:** T ≈ 1/(8πGM) × 0,54",
            "**Ponto Zero-Fluxo:** E = ½hν × 0,54"
        ]
        for f in formulas:
            st.markdown(f)

    # ---------- Validação Rápida (tab6) - NOVA ----------
    with tab6:
        titulo_ajudado("🔍 Validação Rápida de Padrões")
        st.markdown("Insira um número e veja se ele se aproxima de alguma constante fundamental.")
        valor_teste = st.number_input("Valor para teste:", value=1.618, format="%.6f")
        tolerancia = st.slider("Tolerância percentual (%)", 0.1, 10.0, 1.0, 0.1)
        padroes = encontrar_padroes(valor_teste, tolerancia)
        if padroes:
            st.success("✅ Padrões encontrados!")
            for nome, dados in padroes.items():
                st.write(f"- **{nome}**: constante = {dados['constante']:.6f}, desvio = {dados['desvio_%']:.3f}%")
        else:
            st.info("Nenhum padrão encontrado dentro da tolerância.")
        # Mostrar também redução teosófica
        st.write(f"Redução teosófica do valor: {reduzir_teosoficamente(valor_teste)}")

# =============================================================================
# PÁGINA: TEMPO ESPIRALADO (ORIGINAL)
# =============================================================================
elif pagina == "⏳ Tempo Espiralado":
    titulo_ajudado("⏳ Tempo Espiralado - Novo Calendário Cósmico", nivel="title")
    st.markdown("""
    ## O Tempo como uma Espiral de Frequência 432Hz

    Neste sistema, o tempo é medido em:
    - **Pulsos**: Batidas na frequência de 432Hz (1 pulso = 1/432 segundos)
    - **Vibes**: 432 Pulsos (≈1 segundo harmônico)
    - **Giros**: 9 Vibes (≈9 segundos)
    - **Ciclos**: 9 Giros (≈81 segundos)
    - **Eras**: 9 Ciclos (≈729 segundos)

    Tudo baseado nos números sagrados 3, 6 e 9.
    """)

    placeholder = st.empty()
    for _atualizacao in range(1):  # Uma renderização por execução; evita bloquear a interface.
        pulsos = relogio.get_pulsos_desde_singularidade()
        tempo = relogio.converter_pulsos(pulsos)

        with placeholder.container():
            col1, col2 = st.columns(2)
            with col1:
                titulo_ajudado("Tempo Atual no Fluxo")
                st.metric("Eras", tempo['eras'])
                st.metric("Ciclos", tempo['ciclos'])
                st.metric("Giros", tempo['giros'])
                st.metric("Vibes", tempo['vibes'])
                st.metric("Pulsos", tempo['pulsos'])
                st.write(f"**Frequência:** {FREQUENCIA_BASE} Hz (432Hz)")

            with col2:
                titulo_ajudado("Equivalente Gregoriano")
                agora = datetime.datetime.now(pytz.UTC)
                st.write(f"**Data/Hora:** {agora.strftime('%Y-%m-%d %H:%M:%S %Z')}")
                delta = agora - SINGULARIDADE
                st.write(f"**Tempo desde Singularidade:** {delta}")

            titulo_ajudado("Visualização 3D do Tempo Espiralado")
            fig = relogio.plotar_espiral_temporal(pulsos)
            st.pyplot(fig)

            st.write("""
            **Legenda:**
            - Linha azul: Fluxo do tempo espiralado
            - Ponto vermelho: Momento atual
            - Estrelas douradas: Pontos 3-6-9 no ciclo
            """)

        if not auto_update:
            break
        # A atualização ocorre quando o Streamlit reexecuta o script.

# =============================================================================
# PÁGINA: VISUALIZAÇÕES (ORIGINAL, com novas adições)
# =============================================================================
elif pagina == "📊 Visualizações":
    titulo_ajudado("📊 Visualizações do Fluxo Matemático", nivel="title")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌀 Ciclo 1-2-4-8-7-5", "🔺 Geometria 3-6-9", "📈 Comparativo", "🔥 Mapa de Calor", "🌌 Galáxia interativa"])

    with tab1:
        titulo_ajudado("Sequência de Dobramento com Redução Teosófica")
        iteracoes = st.slider("Número de iterações:", 10, 100, 30, key="iteracoes_seq")
        fig = plot_sequencia_reducao(iteracoes)
        st.pyplot(fig)
        st.write("""
        **Interpretação:**
        - Cada passo dobra o valor anterior
        - Aplicamos a redução teosófica
        - Padrão infinito: 1 → 2 → 4 → 8 → 7 → 5 → 1...
        - Total do ciclo: 1+2+4+8+7+5 = 27 → 2+7=9
        """)

    with tab2:
        titulo_ajudado("Geometria Sagrada 3-6-9")
        fig = plot_geometria_369()
        st.pyplot(fig)
        st.write("""
        **Significado:**
        - 3: Força criativa, ação
        - 6: Equilíbrio, harmonia
        - 9: Compleção, transição
        - Juntos formam um triângulo equilátero perfeito
        """)

    with tab3:
        titulo_ajudado("Comparativo Matemática Clássica vs Fluxo")
        df = pd.DataFrame({
            "Operação": ["Soma 8+8", "Multiplicação 7×7", "Potência 3^4", "Fibonacci(10)"],
            "Clássico": [16, 49, 81, 55],
            "Fluxo": [7, 4, 9, 1]
        })
        st.dataframe(df.style.applymap(lambda x: 'background-color: gold' if x == 9 else '', subset=['Fluxo']))
        st.write("""
        **Observações:**
        - O número 9 no Fluxo Matemático representa completude
        - Padrões emergem quando comparamos os dois sistemas
        - A matemática clássica mostra a quantidade, o Fluxo mostra a qualidade
        """)

    with tab4:
        titulo_ajudado("Mapa de Calor da Redução Teosófica")
        fig = plot_padroes_calor()
        st.pyplot(fig)
        st.write("Mapa de calor da redução teosófica dos produtos de 1 a 20.")

    with tab5:
        titulo_ajudado("🌌 Galáxia espiral interativa")
        st.caption("Simulação matemática/artística para explorar braços, rotação e inclinação — não representa dados astronômicos reais.")
        g1, g2, g3 = st.columns(3)
        with g1:
            bracos_galaxia = st.slider("Braços espirais", 2, 8, 4, key="galaxia_bracos")
            estrelas_galaxia = st.slider("Quantidade de estrelas", 300, 3000, 1400, step=100, key="galaxia_estrelas")
        with g2:
            rotacao_galaxia = st.slider("Torção dos braços", 0.2, 2.5, 1.0, step=0.1, key="galaxia_rotacao")
            abertura_galaxia = st.slider("Dispersão estelar", 0.05, 0.8, 0.32, step=0.01, key="galaxia_abertura")
        with g3:
            inclinacao_galaxia = st.slider("Ângulo de observação", 5, 85, 24, key="galaxia_inclinacao")
        st.pyplot(plotar_galaxia_fluxo(bracos_galaxia, estrelas_galaxia, rotacao_galaxia,
                                      abertura_galaxia, inclinacao_galaxia), use_container_width=True)
        st.info("Mude os controles e observe a estrutura espacial mudar. O modelo é ilustrativo; não deve ser interpretado como mapa físico da Via Láctea.")


# =============================================================================
# PÁGINA: ACELERADOR DE PARTÍCULAS (ORIGINAL)
# =============================================================================
elif pagina == "🌀 Acelerador de Partículas":
    titulo_ajudado("🌀 Simulador de Acelerador de Partículas", nivel="title")
    st.markdown("Cálculos desde a física clássica até o fluxo, com visualização.")

    col1, col2 = st.columns(2)
    with col1:
        particula = st.selectbox("Partícula", ["Elétron", "Próton", "Nêutron", "Fóton", "Personalizada"])
        massas = {
            "Elétron": 9.1093837e-31,
            "Próton": 1.6726219e-27,
            "Nêutron": 1.6749275e-27,
            "Fóton": 0.0,
            "Personalizada": 1e-30
        }
        massa = massas[particula]
        if particula == "Personalizada":
            massa = st.number_input("Massa (kg)", value=1e-30, format="%.3e")
    with col2:
        energia = st.number_input("Energia (valor)", value=1.0, step=0.1)
        unidade = st.selectbox("Unidade", ["eV", "keV", "MeV", "GeV", "TeV"])
        fatores = {'eV': 1.602176634e-19, 'keV': 1.602176634e-16, 'MeV': 1.602176634e-13,
                   'GeV': 1.602176634e-10, 'TeV': 1.602176634e-7}
        energia_J = energia * fatores[unidade]

    N_part = st.number_input("N para F(N)", value=29, step=1, key="N_part")
    const_part = st.number_input("Constante de fluxo", value=MARC, format="%.3f")

    if st.button("Simular Colisão", key="simular"):
        with st.spinner("Acelerando partículas..."):
            res = simular_acelerador(massa, energia_J, N_part, const_part)

        colA, colB, colC, colD = st.columns(4)
        with colA:
            st.metric("Velocidade clássica", f"{res['v_class']:.3e} m/s")
            st.metric("Momento clássico", f"{res['p_class']:.3e} kg·m/s")
        with colB:
            st.metric("Fator γ (Lorentz)", f"{res['gamma']:.3f}")
            st.metric("Massa relativística", f"{res['m_rel']:.3e} kg")
        with colC:
            st.metric("λ de Broglie", f"{res['lambda_db']:.3e} m")
            st.metric("Probabilidade quântica", f"{res['prob']:.3f}")
        with colD:
            st.metric("Velocidade Fluxo", f"{res['v_flux']:.3e} m/s")
            st.metric("Energia Fluxo", f"{res['E_flux']:.3e} J")
            st.caption(f"F({N_part}) = {res['f']:.3f}")

        st.info(f"Estado de entrelaçamento: {res['ent_rel']}")
        registrar_calculo_fluxo("Acelerador", f"Colisão · {particula} · {energia:g} {unidade}",
            {"Velocidade clássica": res['v_class'], "Velocidade Fluxo": res['v_flux'], "Momento clássico": res['p_class'], "Fator Lorentz": res['gamma'], "Massa relativística": res['m_rel'], "Comprimento de onda de Broglie": res['lambda_db'], "Energia Fluxo": res['E_flux']},
            {"Velocidade clássica": "m/s", "Velocidade Fluxo": "m/s", "Momento clássico": "kg·m/s", "Fator Lorentz": "adimensional", "Massa relativística": "kg", "Comprimento de onda de Broglie": "m", "Energia Fluxo": "J"},
            f"Massa da partícula={massa:.4e} kg; energia de entrada={energia_J:.4e} J; F(N)={res['f']:.4g}")

        fig, ax = plt.subplots(figsize=(6, 4))
        theta = np.linspace(0, 2*np.pi, 100)
        r_class = res['v_class'] / 1e8
        r_flux = res['v_flux'] / 1e8
        ax.plot(r_class * np.cos(theta), r_class * np.sin(theta), 'o-', label='Clássica', markersize=2, color='orange')
        ax.plot(r_flux * np.cos(theta), r_flux * np.sin(theta), 'o-', label='Fluxo', markersize=2, color='purple')
        ax.set_aspect('equal')
        ax.legend()
        ax.set_title("Trajetória no acelerador (vista superior)")
        ax.grid(True)
        st.pyplot(fig)
        plt.close(fig)

# =============================================================================
# PÁGINA: GEOMETRIA SAGRADA (ORIGINAL)
# =============================================================================
elif pagina == "△ Geometria Sagrada":
    titulo_ajudado("△ Geometria Sagrada no Fluxo", nivel="title")
    sub_geo = st.radio("Escolha", ["Pitágoras-Fluxo", "Espiral Áurea", "Bobina Áurea de Tesla"], horizontal=True)

    if sub_geo == "Pitágoras-Fluxo":
        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input("Cateto a", value=3.0)
        with col2:
            b = st.number_input("Cateto b", value=4.0)
        with col3:
            modo = st.selectbox("Modo", ["classico", "aureo", "fluxo", "completo"])
        classico, fluxo = pitagoras_fluxo(a, b, modo)
        st.write(f"**Hipotenusa clássica:** {classico:.6f}")
        st.write(f"**Hipotenusa fluxo:** {fluxo:.6f}")
        registrar_calculo_fluxo("Geometria Sagrada", "Pitágoras-Fluxo", {"Hipotenusa clássica": classico, "Hipotenusa Fluxo": fluxo, "Cateto a": a, "Cateto b": b}, {"Hipotenusa clássica": "unidade dos catetos", "Hipotenusa Fluxo": "unidade dos catetos"}, f"Modo selecionado: {modo}")
        fig = plot_triangulo(a, b, fluxo)
        st.pyplot(fig)
        plt.close(fig)

    elif sub_geo == "Espiral Áurea":
        col1, col2 = st.columns(2)
        with col1:
            angulo = st.slider("Ângulo θ (rad)", 0.0, 4*np.pi, 2.0, step=0.1)
        with col2:
            f_esp = st.number_input("Fator de fluxo", value=fator_fluxo(29), step=0.1)
        x, y, r = espiral_aurea(angulo, f_esp)
        st.write(f"**Raio:** {r:.6f}  **Coordenadas:** ({x:.6f}, {y:.6f})")
        registrar_calculo_fluxo("Geometria Sagrada", "Espiral Áurea", {"Raio": r, "Coordenada X": x, "Coordenada Y": y, "Ângulo": angulo, "Fator de fluxo": f_esp}, {"Raio": "unidade do modelo", "Coordenada X": "unidade do modelo", "Coordenada Y": "unidade do modelo", "Ângulo": "rad"})
        fig = plot_espiral_aurea(f_esp, 4*np.pi)
        ax = fig.gca()
        ax.scatter([x], [y], color='red', s=50)
        st.pyplot(fig)
        plt.close(fig)

    elif sub_geo == "Bobina Áurea de Tesla":
        col1, col2, col3 = st.columns(3)
        with col1:
            N_esp = st.number_input("Número de espiras", value=100, step=1)
        with col2:
            raio = st.number_input("Raio (m)", value=0.1, step=0.01)
        with col3:
            comp = st.number_input("Comprimento (m)", value=0.5, step=0.01)
        modo_bob = st.selectbox("Modo de cálculo", ["classico", "aureo", "fluxo"])
        L = indutancia_bobina(N_esp, raio, comp, modo_bob)
        st.metric("Indutância", f"{L:.6e} H")
        L_class = indutancia_bobina(N_esp, raio, comp, 'classico')
        L_aureo = indutancia_bobina(N_esp, raio, comp, 'aureo')
        L_flux = indutancia_bobina(N_esp, raio, comp, 'fluxo')
        st.write(f"**Comparação:** Clássico = {L_class:.6e} H, Áureo = {L_aureo:.6e} H, Fluxo = {L_flux:.6e} H")
        registrar_calculo_fluxo("Geometria Sagrada", "Bobina Áurea de Tesla", {"Indutância clássica": L_class, "Indutância áurea": L_aureo, "Indutância Fluxo": L_flux, "Espiras": N_esp, "Raio": raio, "Comprimento": comp}, {"Indutância clássica": "H", "Indutância áurea": "H", "Indutância Fluxo": "H", "Raio": "m", "Comprimento": "m"}, f"Modo exibido: {modo_bob}")

# =============================================================================
# NOVA PÁGINA: PADRÕES E VALIDAÇÕES
# =============================================================================
elif pagina == "🔍 Padrões e Validações":
    titulo_ajudado("🔍 Padrões e Validações", nivel="title")
    st.markdown("""
    ## Encontre Padrões Ocultos nos Números

    Esta seção permite que você insira um número e veja se ele se aproxima de constantes fundamentais como π, φ, 1,80, 0,54, 0,18, etc.
    Você também pode gerar sequências de Fibonacci e analisar suas reduções teosóficas.
    """)

    tab1, tab2, tab3 = st.tabs(["🔎 Validação de Número", "🌀 Fibonacci no Fluxo", "📐 Aproximações de π e φ"])

    with tab1:
        titulo_ajudado("Validar um Número")
        valor = st.number_input("Digite um número:", value=1.6180339, format="%.7f")
        tolerancia = st.slider("Tolerância percentual (%)", 0.01, 10.0, 0.5, 0.01)
        padroes = encontrar_padroes(valor, tolerancia)
        if padroes:
            st.success("✅ Padrões encontrados!")
            for nome, dados in padroes.items():
                st.write(f"- **{nome}**: constante = {dados['constante']:.6f}, desvio = {dados['desvio_%']:.4f}%")
        else:
            st.info("Nenhum padrão encontrado dentro da tolerância.")
        reducao_valor = reduzir_teosoficamente(valor)
        st.write(f"**Redução teosófica:** {reducao_valor}")
        registrar_calculo_fluxo("Padrões e Validações", "Validação de número", {"Valor de entrada": valor, "Redução teosófica": reducao_valor}, {}, f"Tolerância selecionada: {tolerancia:g}% · padrões: {', '.join(padroes.keys()) if padroes else 'nenhum dentro da tolerância'}")

    with tab2:
        titulo_ajudado("Fibonacci e Redução Teosófica")
        n_fib = st.slider("Número de termos de Fibonacci:", 5, 50, 20)
        fibs = fibonacci_reductions(n_fib)
        df_fib = pd.DataFrame(fibs, columns=["Índice", "Fibonacci", "Redução"])
        st.dataframe(df_fib)
        registrar_calculo_fluxo("Análise de Padrões", "Fibonacci e reduções", {f"Fibonacci({idx})": fib for idx, fib, red in fibs[:20]}, {}, f"Quantidade selecionada: {n_fib} termos; valores limitados aos primeiros 20 no painel compartilhado.")
        # Gráfico
        fig, ax = plt.subplots()
        ax.plot(df_fib["Índice"], df_fib["Redução"], marker='o', color='green')
        ax.set_title("Redução Teosófica dos Números de Fibonacci")
        ax.set_xlabel("Índice")
        ax.set_ylabel("Redução")
        ax.grid(True)
        st.pyplot(fig)
        plt.close(fig)
        # Encontrar padrões nos próprios números de Fibonacci
        titulo_ajudado("Padrões nos Números de Fibonacci")
        for idx, fib, red in fibs:
            pad = encontrar_padroes(fib, 1.0)
            if pad:
                st.write(f"Fibonacci({idx}) = {fib} → {', '.join(pad.keys())}")

    with tab3:
        titulo_ajudado("Aproximações de π e φ")
        col1, col2 = st.columns(2)
        with col1:
            st.write("### π (pi)")
            aprox_pi = calcular_pi_aproximacoes()
            for nome, val in aprox_pi.items():
                st.write(f"{nome}: {val:.10f}")
        with col2:
            st.write("### φ (áurea)")
            aprox_phi = calcular_phi_aproximacoes()
            for nome, val in aprox_phi.items():
                st.write(f"{nome}: {val:.10f}")

        st.write("### Relação Gratidão")
        rel_grat = calcular_relacao_gratidao()
        for nome, val in rel_grat.items():
            st.write(f"{nome}: {val:.6f}")

# =============================================================================
# NOVA PÁGINA: TODAS AS MENTES
# =============================================================================
elif pagina == "🧠 Todas as Mentes":
    titulo_ajudado("🧠 Todas as Mentes Matemáticas", nivel="title")
    st.markdown("""
    ## Comparação de Resultados Segundo Diferentes "Mentes"

    Cada "mente" representa uma abordagem matemática ou física diferente:
    - **Clássica**: Matemática tradicional.
    - **Fluxo**: Aplicação das constantes de Catharino (MARC, DEUS, GRATIDAO).
    - **Tesla**: Ênfase nos números 3, 6, 9 e vibrações.
    - **Einstein**: Relatividade e equivalência massa-energia.
    - **Pitágoras**: Geometria e harmonia.
    - **Planck**: Escala quântica.
    """)

    # Entrada do usuário
    valor_entrada = st.number_input("Valor de entrada para teste:", value=9.0)
    operacao_mente = st.selectbox("Operação", ["Quadrado", "Cubo", "Raiz Quadrada", "Seno (graus)", "Fatorial (aproximado)"])
    
    resultados = {}
    if operacao_mente == "Quadrado":
        classico = valor_entrada ** 2
        fluxo = classico * MARC
        tesla = classico * 0.369  # exemplo
        einstein = classico * (C_LUZ / 1e8)  # só para ter variação
        pitagoras = classico * PHI
        planck = classico * H_PLANCK * 1e34  # escala
    elif operacao_mente == "Cubo":
        classico = valor_entrada ** 3
        fluxo = classico * MARC
        tesla = classico * 0.369
        einstein = classico * (C_LUZ / 1e8)
        pitagoras = classico * PHI
        planck = classico * H_PLANCK * 1e34
    elif operacao_mente == "Raiz Quadrada":
        classico = math.sqrt(valor_entrada)
        fluxo = classico * MARC
        tesla = classico * 0.369
        einstein = classico * (C_LUZ / 1e8)
        pitagoras = classico * PHI
        planck = classico * H_PLANCK * 1e34
    elif operacao_mente == "Seno (graus)":
        classico = math.sin(math.radians(valor_entrada))
        fluxo = classico * MARC
        tesla = classico * 0.369
        einstein = classico * (C_LUZ / 1e8)
        pitagoras = classico * PHI
        planck = classico * H_PLANCK * 1e34
    elif operacao_mente == "Fatorial (aproximado)":
        # Stirling approximation for large numbers
        n = int(valor_entrada)
        if n <= 0:
            classico = 1
        else:
            classico = math.sqrt(2*math.pi*n) * (n/math.e)**n
        fluxo = classico * MARC
        tesla = classico * 0.369
        einstein = classico * (C_LUZ / 1e8)
        pitagoras = classico * PHI
        planck = classico * H_PLANCK * 1e34

    resultados = {
        "Clássica": classico,
        "Fluxo (MARC)": fluxo,
        "Tesla (3-6-9)": tesla,
        "Einstein (c)": einstein,
        "Pitágoras (φ)": pitagoras,
        "Planck (h)": planck,
    }

    df_mentes = pd.DataFrame(list(resultados.items()), columns=["Mente", "Resultado"])
    st.dataframe(df_mentes.style.format({"Resultado": "{:.6e}"}))

    # Gráfico comparativo
    fig, ax = plt.subplots()
    nomes = list(resultados.keys())
    valores = list(resultados.values())
    ax.barh(nomes, valores, color=['blue', 'purple', 'orange', 'red', 'green', 'cyan'])
    ax.set_xscale('log')
    ax.set_xlabel('Resultado (escala log)')
    ax.set_title('Comparação entre Mentes')
    st.pyplot(fig)
    plt.close(fig)

    # Validação de padrões em cada resultado
    titulo_ajudado("Padrões encontrados em cada mente")
    for mente, val in resultados.items():
        pad = encontrar_padroes(val, 5.0)  # tolerância maior
        if pad:
            st.write(f"**{mente}**: {', '.join(pad.keys())}")

# =============================================================================
# NOVA PÁGINA: GRAVIDADE QUÂNTICA
# =============================================================================
elif pagina == "🌀 Gravidade Quântica":
    titulo_ajudado("🌀 Gravidade Quântica e Escala de Planck", nivel="title")
    st.markdown("""
    ## Explorando a Física na Escala de Planck

    A gravidade quântica tenta unificar a relatividade geral com a mecânica quântica.
    Aqui calculamos algumas quantidades na escala de Planck e aplicamos o fluxo.
    """)

    col1, col2 = st.columns(2)
    with col1:
        titulo_ajudado("Constantes de Planck")
        st.write(f"Massa de Planck: {PLANCK_MASSA:.3e} kg")
        st.write(f"Comprimento de Planck: {PLANCK_COMPRIMENTO:.3e} m")
        st.write(f"Tempo de Planck: {PLANCK_TEMPO:.3e} s")
        st.write(f"Energia de Planck: {PLANCK_ENERGIA:.3e} J")
        st.write(f"Gravidade Quântica (exemplo): {GRAVIDADE_QUANTICA:.3e} m/s²")

    with col2:
        titulo_ajudado("Relações com o Fluxo")
        st.write(f"Massa Planck × MARC: {PLANCK_MASSA * MARC:.3e} kg")
        st.write(f"Comp. Planck × DEUS: {PLANCK_COMPRIMENTO * DEUS:.3e} m")
        st.write(f"Tempo Planck × GRATIDAO: {PLANCK_TEMPO * GRATIDAO:.3e} s")

    titulo_ajudado("Cálculos de Gravidade Quântica")
    escolha = st.selectbox("Escolha o cálculo", ["Raio de Schwarzschild", "Temperatura de Hawking", "Energia do Ponto Zero", "Probabilidade de Emaranhamento"])

    if escolha == "Raio de Schwarzschild":
        massa = st.number_input("Massa (kg)", value=PLANCK_MASSA, format="%.3e")
        classico, fluxo = calcular_raio_schwarzschild(massa, MARC)
        st.write(f"**Clássico:** Rs = {classico:.3e} m")
        st.write(f"**Fluxo (×MARC):** Rs = {fluxo:.3e} m")
    elif escolha == "Temperatura de Hawking":
        massa = st.number_input("Massa (kg)", value=PLANCK_MASSA, format="%.3e")
        classico, fluxo = calcular_temperatura_hawking(massa, MARC)
        st.write(f"**Clássico (aprox):** T = {classico:.3e} K (escala adimensional)")
        st.write(f"**Fluxo:** T = {fluxo:.3e}")
    elif escolha == "Energia do Ponto Zero":
        freq = st.number_input("Frequência de corte (Hz)", value=1e43, format="%.3e")
        classico, fluxo = calcular_energia_ponto_zero(freq, MARC)
        st.write(f"**Clássico:** E = {classico:.3e} J")
        st.write(f"**Fluxo:** E = {fluxo:.3e} J")
    elif escolha == "Probabilidade de Emaranhamento":
        dist = st.number_input("Distância (m)", value=PLANCK_COMPRIMENTO, format="%.3e")
        classico, fluxo = calcular_longa_distancia_emaranhamento(dist, MARC)
        st.write(f"**Clássico:** P ≈ {classico:.3e}")
        st.write(f"**Fluxo:** P ≈ {fluxo:.3e}")

# =============================================================================
# NOVA PÁGINA: ANÁLISE DE PADRÕES
# =============================================================================
elif pagina == "📈 Análise de Padrões":
    titulo_ajudado("📈 Análise de Padrões Numéricos", nivel="title")
    st.markdown("""
    ## Ferramentas para Análise de Sequências e Constantes

    Explore como números se relacionam com π, φ, Fibonacci e as constantes do fluxo.
    """)

    tab1, tab2, tab3 = st.tabs(["🔢 Sequência Personalizada", "📊 Correlação com Constantes", "🌀 Geração de Padrões"])

    with tab1:
        titulo_ajudado("Analisar uma Sequência")
        seq_input = st.text_area("Digite uma sequência de números separados por vírgula:", "1,1,2,3,5,8,13,21,34")
        try:
            sequencia = [float(x.strip()) for x in seq_input.split(",")]
            st.write("Sequência:", sequencia)
            # Calcular reduções
            reducoes = [reduzir_teosoficamente(x) for x in sequencia]
            st.write("Reduções teosóficas:", reducoes)
            registrar_calculo_fluxo("Análise de Padrões", "Sequência personalizada", {f"Termo {i+1}": v for i, v in enumerate(sequencia[:20])}, {}, f"Reduções calculadas: {reducoes[:20]}")
            # Mostrar a série no gráfico e na ponte para o observatório.
            fig_seq, ax_seq = plt.subplots(figsize=(9, 3.5))
            ax_seq.plot(range(1, len(sequencia)+1), sequencia, marker="o", label="Valores de entrada")
            ax_seq.plot(range(1, len(reducoes)+1), reducoes, marker=".", label="Redução teosófica")
            ax_seq.set_xlabel("Posição na sequência"); ax_seq.set_ylabel("Valor")
            ax_seq.set_title("Sequência e redução · dados desta análise")
            ax_seq.grid(True, alpha=0.22); ax_seq.legend(); fig_seq.tight_layout()
            st.pyplot(fig_seq, use_container_width=True); plt.close(fig_seq)
            # Encontrar padrões em cada elemento
            for i, val in enumerate(sequencia):
                pad = encontrar_padroes(val, 1.0)
                if pad:
                    st.write(f"Elemento {i+1} ({val}) → {', '.join(pad.keys())}")
        except:
            st.error("Formato inválido. Use números separados por vírgula.")

    with tab2:
        titulo_ajudado("Correlação com Constantes")
        # Gerar uma faixa de valores e ver quais são próximos das constantes
        inicio = st.number_input("Início do intervalo", value=0.0)
        fim = st.number_input("Fim do intervalo", value=10.0)
        passos = st.number_input("Número de pontos", value=100, step=1)
        valores = np.linspace(inicio, fim, int(passos))
        const_list = [("π", PI), ("φ", PHI), ("Gratidão", GRATIDAO), ("Marc", MARC), ("Deus", DEUS), ("432", FREQUENCIA_BASE)]
        resultados_corr = []
        for val in valores:
            for nome, const in const_list:
                prox, _ = is_close_to_constant(val, const, 0.5)
                if prox:
                    resultados_corr.append((val, nome, const))
        if resultados_corr:
            df_corr = pd.DataFrame(resultados_corr, columns=["Valor", "Constante", "Valor Constante"])
            st.dataframe(df_corr)
            registrar_calculo_fluxo("Análise de Padrões", "Correlação com constantes", {f"Correspondência {i+1} · valor": linha[0] for i, linha in enumerate(resultados_corr[:20])}, {}, f"Intervalo [{inicio:g}, {fim:g}], {int(passos)} pontos; {len(resultados_corr)} aproximações encontradas com tolerância de 0,5%.")
        else:
            st.info("Nenhuma correlação encontrada no intervalo com tolerância 0.5%.")

    with tab3:
        titulo_ajudado("Gerador de Padrões")
        st.write("Gerar números que são combinações das constantes.")
        const1 = st.selectbox("Constante 1", ["π", "φ", "Gratidão", "Marc", "Deus"])
        const2 = st.selectbox("Constante 2", ["π", "φ", "Gratidão", "Marc", "Deus"])
        oper = st.selectbox("Operação", ["+", "-", "*", "/"])
        mapa = {"π": PI, "φ": PHI, "Gratidão": GRATIDAO, "Marc": MARC, "Deus": DEUS}
        v1 = mapa[const1]
        v2 = mapa[const2]
        if oper == "+":
            res = v1 + v2
        elif oper == "-":
            res = v1 - v2
        elif oper == "*":
            res = v1 * v2
        elif oper == "/":
            res = v1 / v2 if v2 != 0 else float('inf')
        st.write(f"Resultado: {res}")
        registrar_calculo_fluxo("Análise de Padrões", "Combinação de constantes", {"Constante 1": v1, "Constante 2": v2, "Resultado": res}, {}, f"Operação: {const1} {oper} {const2}")
        # Verificar se o resultado se aproxima de alguma constante
        pad = encontrar_padroes(res, 0.5)
        if pad:
            st.success("✅ Este resultado é próximo de: " + ", ".join(pad.keys()))
        else:
            st.info("Nenhuma correspondência próxima.")

# =============================================================================
# PÁGINA: PDF EXPLICATIVO (ORIGINAL, com nova função já expandida)
# =============================================================================
elif pagina == "📚 PDF Explicativo":
    titulo_ajudado("📚 Gerar PDF Explicativo", nivel="title")
    nome = st.text_input("Seu nome:", "Marcelo Jubilado Catharino")
    email = st.text_input("Seu email:", "marcelo@universoaureo.com")

    if st.button("Gerar PDF Completo"):
        with st.spinner("Criando documento..."):
            pdf_bytes = gerar_pdf_completo(nome, email)
            b64 = base64.b64encode(pdf_bytes.read()).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="fluxo_matematico_expandido.pdf">📥 Clique para baixar o PDF</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("PDF gerado com sucesso!")

# =============================================================================
# PÁGINA: RELÓGIO QUÂNTICO (ORIGINAL)
# =============================================================================
elif pagina == "🕒 Relógio Quântico":
    titulo_ajudado("🕒 Relógio Quântico com Projeção para Singularidade", nivel="title")
    st.markdown("""
    ## O Tempo como uma Espiral Quântica

    Este relógio representa:
    - **Tempo atual**: Ponteiro vermelho
    - **Projeção para singularidade**: Ponteiro azul tracejado (fase oposta)
    - **Marcadores dourados**: Pontos 3-6-9 no ciclo temporal
    - **Círculos concêntricos**: Dimensões temporais sobrepostas
    """)

    fuso_relogio = st.selectbox(
        "Fuso horário para a leitura digital",
        ["America/Sao_Paulo", "UTC", "Europe/London", "America/New_York", "Asia/Tokyo"],
        index=0,
        format_func=lambda f: {"America/Sao_Paulo": "Brasil · Brasília", "UTC": "UTC",
                               "Europe/London": "Londres", "America/New_York": "Nova York",
                               "Asia/Tokyo": "Tóquio"}.get(f, f),
        key="fuso_relogio_quantico"
    )
    placeholder = st.empty()
    for _atualizacao in range(1):  # Uma renderização por execução; evita bloquear a interface.
        with placeholder.container():
            fig = relogio.plotar_relogio_quantico()
            st.pyplot(fig)
            agora = datetime.datetime.now(pytz.UTC)
            agora_local = agora.astimezone(pytz.timezone(fuso_relogio))
            delta = agora - SINGULARIDADE
            total_segundos = int(delta.total_seconds())
            dias, resto = divmod(total_segundos, 86400)
            horas, resto = divmod(resto, 3600)
            minutos, segundos = divmod(resto, 60)
            pulsos_atuais = relogio.get_pulsos_desde_singularidade()
            tempo_fluxo = relogio.converter_pulsos(pulsos_atuais)
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Hora selecionada", agora_local.strftime("%H:%M:%S"))
                st.caption(agora_local.strftime("%A, %d/%m/%Y · %Z"))
            with c2:
                st.metric("Tempo decorrido", f"{dias:,} dias".replace(",", "."))
                st.caption(f"{horas:02d}h {minutos:02d}m {segundos:02d}s além dos dias")
            with c3:
                st.metric("Pulsos calculados", f"{pulsos_atuais:,}".replace(",", "."))
                st.caption(f"Eras {tempo_fluxo['eras']} · Ciclos {tempo_fluxo['ciclos']} · Giros {tempo_fluxo['giros']}")
            st.caption("A leitura é atualizada quando a página é reexecutada; use “Atualizar agora” na barra lateral para recalcular.")
            st.write("""
            **Interpretação:**
            - O tempo flui em espirais quânticas, não linearmente
            - Cada volta completa representa um ciclo completo
            - A singularidade é o ponto de origem (12 horas)
            - Os marcadores 3-6-9 representam pontos de transição dimensional
            """)
        if not auto_update:
            break
        # A atualização ocorre quando o Streamlit reexecuta o script.

# =============================================================================
# PÁGINA: CALENDÁRIO CLÁSSICO (ORIGINAL)
# =============================================================================
elif pagina == "📅 Calendário Clássico":
    titulo_ajudado("📅 Calendário e Relógio Clássico", nivel="title")
    st.markdown("""
    ## Visualização Tradicional do Tempo

    Esta seção mostra o tempo na forma convencional que estamos habituados,
    enquanto mantemos a conexão com o Fluxo Matemático.
    """)

    placeholder = st.empty()
    for _atualizacao in range(1):  # Uma renderização por execução; evita bloquear a interface.
        with placeholder.container():
            agora = datetime.datetime.now(pytz.UTC)
            data_formatada = agora.strftime("%A, %d de %B de %Y")
            hora_formatada = agora.strftime("%H:%M:%S")

            col1, col2 = st.columns(2)
            with col1:
                titulo_ajudado("Data Atual")
                st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{data_formatada}</h1>",
                           unsafe_allow_html=True)

                # Calendário do mês
                hoje = agora.day
                mes = agora.month
                ano = agora.year
                # Primeiro dia do mês
                primeiro_dia = datetime.datetime(ano, mes, 1)
                if mes == 12:
                    dias_no_mes = 31
                else:
                    dias_no_mes = (datetime.datetime(ano, mes + 1, 1) - datetime.timedelta(days=1)).day
                dia_semana = primeiro_dia.weekday()  # 0=Segunda, 6=Domingo

                semanas = []
                semana = [""] * dia_semana
                for dia in range(1, dias_no_mes + 1):
                    semana.append(str(dia))
                    if len(semana) == 7:
                        semanas.append(semana)
                        semana = []
                if semana:
                    semanas.append(semana + [""] * (7 - len(semana)))

                df_calendario = pd.DataFrame(semanas, columns=["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"])
                st.dataframe(df_calendario.style.applymap(lambda x: 'background-color: gold' if x == str(hoje) else ''))

            with col2:
                titulo_ajudado("Hora Atual")
                st.markdown(f"<h1 style='text-align: center; color: #2196F3;'>{hora_formatada}</h1>",
                           unsafe_allow_html=True)

                # Mostrar também no formato do Fluxo Matemático
                pulsos = relogio.get_pulsos_desde_singularidade()
                tempo_fluxo = relogio.converter_pulsos(pulsos)

                st.write("### No Fluxo Matemático:")
                st.write(f"- Eras: {tempo_fluxo['eras']}")
                st.write(f"- Ciclos: {tempo_fluxo['ciclos']}")
                st.write(f"- Giros: {tempo_fluxo['giros']}")
                st.write(f"- Vibes: {tempo_fluxo['vibes']}")
                st.write(f"- Pulsos: {tempo_fluxo['pulsos']}")

                # Redução teosófica da data e hora
                data_num = int(agora.strftime("%Y%m%d"))
                hora_num = int(agora.strftime("%H%M%S"))
                st.write("### Redução Teosófica:")
                st.write(f"- Data ({data_num}): {reduzir_teosoficamente(data_num)}")
                st.write(f"- Hora ({hora_num}): {reduzir_teosoficamente(hora_num)}")

            st.write("""
            **Conexão com o Fluxo Matemático:**
            - Mesmo na visualização clássica, podemos perceber os padrões numéricos
            - A redução teosófica revela a essência vibracional de cada momento
            - O calendário mostra a estrutura cíclica do tempo
            """)

        if not auto_update:
            break
        # A atualização ocorre quando o Streamlit reexecuta o script.

# =============================================================================
# PÁGINA: SINGULARIDADE (ORIGINAL)
# =============================================================================
elif pagina == "🌀 Singularidade":
    titulo_ajudado("🌀 Singularidade - A Unificação dos Padrões", nivel="title")
    st.markdown("""
    ## O Ponto de Convergência de Todas as Dimensões

    A singularidade é o momento onde todas as dualidades se encontram,
    onde o 9 se manifesta como o portal entre ciclos, e onde as constantes
    MARC, DEUS e GRATIDAO se alinham para revelar a unidade subjacente.

    Nesta página, exploramos visualizações que convergem para a singularidade.
    """)

    # Gráfico 1: Espiral 3D com ênfase no ponto de singularidade
    titulo_ajudado("Espiral Temporal Convergindo para a Singularidade")
    pulsos = relogio.get_pulsos_desde_singularidade()
    total_pontos = 1000
    theta = np.linspace(0, 12 * np.pi, total_pontos)
    z = np.linspace(0, 10, total_pontos)
    r = z**0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Destacar o ponto de singularidade (origem)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='blue', alpha=0.5, label='Tempo')
    ax.scatter([0], [0], [0], color='gold', s=200, label='Singularidade', marker='*')
    ax.set_title("Convergência para a Singularidade")
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

    # Gráfico 2: Função que mostra a convergência das constantes
    titulo_ajudado("Convergência das Constantes M, D, G")
    x_vals = np.linspace(0, 2*np.pi, 100)
    y_marc = MARC * np.sin(x_vals)
    y_deus = DEUS * np.cos(x_vals)
    y_grat = GRATIDAO * np.sin(2*x_vals) * np.cos(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_marc, label='Marc (0,54)')
    ax.plot(x_vals, y_deus, label='Deus (0,18)')
    ax.plot(x_vals, y_grat, label='Gratidão (1,80)')
    ax.axhline(y=0, color='black', linestyle='--')
    ax.set_xlabel('Fase angular')
    ax.set_ylabel('Amplitude')
    ax.set_title('Interferência das Constantes')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    plt.close(fig)

    # Gráfico 3: Mapa de calor da redução teosófica
    titulo_ajudado("Mapa de Calor da Redução Teosófica")
    fig = plot_padroes_calor()
    st.pyplot(fig)
    plt.close(fig)

    # Tabela com valores próximos à singularidade
    titulo_ajudado("Valores Reduzidos de Números Significativos")
    nums = [9, 27, 54, 108, 216, 432, 864, 1728]
    dados = {'Número': nums, 'Redução': [reduzir_teosoficamente(n) for n in nums]}
    df = pd.DataFrame(dados)
    st.table(df)

    st.markdown("""
    ### Observação Final
    A singularidade não é um ponto estático, mas um processo contínuo de transformação.
    O 9 é a chave: ele representa o fim de um ciclo e o início de outro, onde
    a matemática clássica se dissolve e o fluxo assume o comando.

    Este aplicativo é uma jornada para explorar esses padrões e, esperamos,
    inspirar uma nova compreensão da realidade.
    """)



# =============================================================================
# IDENTIDADE VISUAL CÓSMICA — CSS responsivo e discreto
# =============================================================================
st.markdown("""
<style>
:root { --fluxo-cyan: #63e6ff; --fluxo-violet: #a78bfa; }
[data-testid="stAppViewContainer"] {
  background:
    radial-gradient(ellipse at 8% 2%, rgba(31, 78, 121, .22), transparent 42%),
    radial-gradient(ellipse at 92% 18%, rgba(92, 45, 145, .17), transparent 38%);
}
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
[data-testid="stMetric"] {
  border: 1px solid rgba(99, 230, 255, .23);
  border-radius: 14px;
  padding: 12px 14px;
  background: linear-gradient(145deg, rgba(21,34,61,.48), rgba(29,20,54,.35));
  box-shadow: 0 4px 18px rgba(0,0,0,.10);
}
[data-testid="stMetricValue"] { font-variant-numeric: tabular-nums; }
.stTabs [data-baseweb="tab-list"] { gap: 7px; }
.stTabs [data-baseweb="tab"] {
  border-radius: 9px 9px 0 0;
  padding: 8px 12px;
}
div.stButton > button, div.stDownloadButton > button {
  border: 1px solid rgba(99,230,255,.38);
  border-radius: 10px;
  transition: transform .15s ease, box-shadow .15s ease;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 15px rgba(99,230,255,.15);
}
[data-testid="stExpander"] { border-radius: 12px; }
@media (prefers-reduced-motion: no-preference) {
  [data-testid="stMetric"] { animation: fluxoFade .35s ease-out both; }
  @keyframes fluxoFade { from { opacity:.72; transform:translateY(3px); } to { opacity:1; transform:translateY(0); } }
}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# OBSERVATÓRIO FLUXO — EXPERIÊNCIA VISUAL INTERATIVA EM TODAS AS PÁGINAS
# =============================================================================
st.markdown("---")
titulo_ajudado(
    "🌌 OBSERVATÓRIO FLUXO · Centro de comando visual",
    nivel="subheader",
    texto=("Painel experimental que conecta frequência, fase, tempo, massa de referência e propagação em modelos gráficos. "
           "Os parâmetros geram visualizações matemáticas; só são grandezas físicas quando a unidade e a equação física correspondente estão explicitamente definidas.")
)
st.caption(f"Página ativa: **{pagina}** · ajuste os controles para recalcular os gráficos em tempo real.")

# Resultados reais enviados pelas páginas de cálculo para o observatório compartilhado.
historico_obs = st.session_state.get("fluxo_observatorio_eventos", [])
with st.expander("🔗 Resultados conectados das outras abas", expanded=bool(historico_obs)):
    if not historico_obs:
        st.info("Ainda não há cálculos enviados ao observatório nesta sessão. Execute um cálculo em Cálculos Duais, Acelerador, Geometria Sagrada ou Análise de Padrões e volte a esta área.")
    else:
        ultimo_obs = historico_obs[-1]
        st.markdown(f"### Último cálculo · {ultimo_obs['area']} / {ultimo_obs['nome']}")
        st.caption(f"Registrado às {ultimo_obs['hora']} · {ultimo_obs.get('detalhe', '')}")
        vals_obs = ultimo_obs.get("valores", {})
        metricas_obs = st.columns(min(4, max(1, len(vals_obs))))
        for i, (nome_val, valor_val) in enumerate(list(vals_obs.items())[:4]):
            with metricas_obs[i]:
                unidade_val = ultimo_obs.get("unidades", {}).get(nome_val, "")
                st.metric(nome_val, f"{valor_val:.5g}" + (f" {unidade_val}" if unidade_val else ""))
        if vals_obs:
            df_ultimo_obs = pd.DataFrame([{"Grandeza": k, "Valor": v, "Unidade": ultimo_obs.get("unidades", {}).get(k, "")}
                                          for k, v in vals_obs.items()])
            st.dataframe(df_ultimo_obs, use_container_width=True, hide_index=True)
            fig_ultimo, ax_ultimo = plt.subplots(figsize=(10, 3.6))
            nomes_ultimo = list(vals_obs.keys())
            valores_ultimo = np.array(list(vals_obs.values()), dtype=float)
            # Índices log/normalizados permitem comparar ordens de grandeza sem apagar o valor original na tabela.
            escalas_ultimo = np.sign(valores_ultimo) * np.log10(1 + np.abs(valores_ultimo))
            barras = ax_ultimo.bar(nomes_ultimo, escalas_ultimo, color=np.where(escalas_ultimo >= 0, "#4cc9f0", "#f72585"))
            ax_ultimo.axhline(0, color="gray", linewidth=0.8)
            ax_ultimo.set_ylabel("sinal × log₁₀(1 + |valor|)")
            ax_ultimo.set_title("Assinatura numérica do último cálculo · escala comprimida")
            ax_ultimo.tick_params(axis="x", labelrotation=25)
            ax_ultimo.grid(axis="y", alpha=0.2); fig_ultimo.tight_layout()
            st.pyplot(fig_ultimo, use_container_width=True); plt.close(fig_ultimo)
            st.caption("O gráfico usa transformação logarítmica com sinal para comparar grandezas de escalas diferentes. Consulte a tabela para os valores originais e suas unidades.")
        if len(historico_obs) > 1:
            with st.expander(f"📚 Histórico da sessão ({len(historico_obs)} registros)"):
                linhas_hist = []
                for evento in historico_obs:
                    for chave, valor in evento.get("valores", {}).items():
                        linhas_hist.append({"Hora": evento["hora"], "Área": evento["area"], "Cálculo": evento["nome"], "Grandeza": chave, "Valor": valor, "Unidade": evento.get("unidades", {}).get(chave, "")})
                st.dataframe(pd.DataFrame(linhas_hist), use_container_width=True, hide_index=True)
                st.download_button("⬇️ Exportar histórico conectado (CSV)", pd.DataFrame(linhas_hist).to_csv(index=False).encode("utf-8-sig"), file_name="historico_observatorio_fluxo.csv", mime="text/csv")
        if st.button("🧹 Limpar histórico conectado", key="limpar_historico_observatorio"):
            st.session_state["fluxo_observatorio_eventos"] = []
            st.rerun()

# Visualização específica da aba ativa: usa automaticamente o último evento da área correspondente.
mapa_areas_pagina = {
    "🧮 Cálculos (Dual)": ("Cálculos Duais", "Cálculos Duais · Física"),
    "🌀 Acelerador de Partículas": ("Acelerador",),
    "△ Geometria Sagrada": ("Geometria Sagrada",),
    "🔍 Padrões e Validações": ("Padrões e Validações", "Análise de Padrões"),
    "📈 Análise de Padrões": ("Análise de Padrões",),
}
areas_ativas = mapa_areas_pagina.get(pagina, ())
eventos_contexto = [e for e in historico_obs if any(e.get("area", "").startswith(a) for a in areas_ativas)]
st.markdown("### 🎯 Visualização vinculada à aba ativa")
if eventos_contexto:
    opcoes_evento = [f"{e.get('hora','—')} · {e.get('area','')} · {e.get('nome','')}" for e in eventos_contexto]
    indice_evento = len(eventos_contexto) - 1
    escolhido = st.selectbox("Cálculo que alimenta este gráfico", options=list(range(len(eventos_contexto))),
                             index=indice_evento, format_func=lambda i: opcoes_evento[i], key="obs_evento_contextual")
    renderizar_grafico_calculo_vinculado(eventos_contexto[escolhido], chave_sufixo="contextual")
    st.caption("O gráfico usa automaticamente um cálculo já registrado na área da página ativa. Para atualizar os dados, volte à operação, execute-a novamente e retorne aqui.")
else:
    st.info("Ainda não há um cálculo registrado para a área desta página. Execute uma operação nela; o gráfico contextual aparecerá aqui automaticamente na próxima renderização.")

# Entradas compartilhadas pelo observatório. Os valores aqui não alteram retroativamente outros cálculos da página.
with st.expander("⚙️ Configurar parâmetros do observatório", expanded=True):
    par1, par2, par3, par4 = st.columns(4)
    with par1:
        obs_frequencia = st.number_input("Frequência de referência (Hz)", min_value=0.01, max_value=1_000_000.0,
                                         value=float(FREQUENCIA_BASE), step=1.0, format="%.2f", key="obs_freq")
    with par2:
        obs_massa = st.number_input("Massa de referência (kg)", min_value=1e-30, max_value=1e30,
                                    value=1.0, step=0.1, format="%.6g", key="obs_mass")
    with par3:
        obs_velocidade = st.number_input("Velocidade de propagação (m/s)", min_value=0.01, max_value=float(C_LUZ),
                                         value=343.0, step=1.0, format="%.3f", key="obs_vel")
    with par4:
        obs_duracao = st.number_input("Janela temporal (s)", min_value=0.001, max_value=1_000_000.0,
                                      value=9.0, step=1.0, format="%.3f", key="obs_time")
    par5, par6, par7 = st.columns(3)
    with par5:
        obs_fase = st.slider("Fase visual (graus)", 0, 360, 0, step=5, key="obs_phase")
    with par6:
        obs_amplitude = st.slider("Amplitude normalizada", 0.1, 5.0, 1.0, step=0.1, key="obs_amp")
    with par7:
        obs_paleta = st.selectbox("Escala cromática", ["plasma", "viridis", "turbo", "inferno", "coolwarm", "magma"], index=0, key="obs_palette")

# Valores calculados e identificados por unidades, sem confundir parâmetros visuais com resultados experimentais.
periodo_obs = 1.0 / obs_frequencia
comprimento_onda_obs = obs_velocidade / obs_frequencia
ciclos_obs = obs_frequencia * obs_duracao
fase_rad_obs = np.deg2rad(obs_fase)
energia_quantum_obs = H_PLANCK * obs_frequencia
energia_classica_obs = 0.5 * obs_massa * obs_velocidade**2
energia_classica_obs = min(energia_classica_obs, 1e300)
frequencia_rotulo = f"{obs_frequencia:,.3f}".replace(",", "X").replace(".", ",").replace("X", ".")

met1, met2, met3, met4, met5 = st.columns(5)
with met1:
    st.metric("Frequência", f"{frequencia_rotulo} Hz")
with met2:
    st.metric("Período", f"{periodo_obs:.6g} s")
with met3:
    st.metric("Comprimento de onda*", f"{comprimento_onda_obs:.6g} m")
with met4:
    st.metric("Ciclos na janela", f"{ciclos_obs:.6g}")
with met5:
    st.metric("Energia do fóton*", f"{energia_quantum_obs:.4e} J")
st.caption("*Comprimento de onda calculado por λ = v/f para a velocidade selecionada. Energia do fóton calculada por E = h·f. A energia cinética clássica ½mv² abaixo usa massa e velocidade de referência; não é energia de fóton.")

obs_tabs = st.tabs([
    "🕰️ Relógio quântico",
    "🌊 Frequência & espectro",
    "🚀 Propagação",
    "🌌 Galáxia 3D",
    "🧬 Padrões & escala de cor",
    "🪐 Campo gravitacional",
    "📐 Equações & resultados"
])

with obs_tabs[0]:
    st.markdown("**Relógio de fase · leitura temporal + mostrador radial**")
    agora_obs = datetime.datetime.now(pytz.UTC)
    delta_obs = agora_obs - SINGULARIDADE
    pulsos_obs = relogio.get_pulsos_desde_singularidade()
    fase_giro_obs = (pulsos_obs % PULSOS_POR_GIRO) / PULSOS_POR_GIRO
    angulo_relogio = (2 * np.pi * fase_giro_obs + fase_rad_obs) % (2 * np.pi)
    fuso_obs = st.selectbox(
        "Fuso horário", ["America/Sao_Paulo", "UTC", "Europe/London", "America/New_York", "Asia/Tokyo"],
        index=0, format_func=lambda f: {
            "America/Sao_Paulo": "Brasil · Brasília", "UTC": "UTC", "Europe/London": "Londres",
            "America/New_York": "Nova York", "Asia/Tokyo": "Tóquio"
        }.get(f, f), key="obs_fuso"
    )
    agora_fuso = agora_obs.astimezone(pytz.timezone(fuso_obs))
    rel1, rel2 = st.columns([1, 2])
    with rel1:
        st.markdown(f"### {agora_fuso.strftime('%H:%M:%S')}")
        st.write(agora_fuso.strftime("%A · %d/%m/%Y · %Z"))
        st.metric("Tempo desde a singularidade", f"{delta_obs.days:,} dias".replace(",", "."))
        st.metric("Pulsos do modelo", f"{pulsos_obs:,}".replace(",", "."))
        st.metric("Fase do giro", f"{fase_giro_obs * 100:.3f}%")
        if st.button("🔄 Atualizar leitura temporal", key="obs_refresh_clock", use_container_width=True):
            st.rerun()
    with rel2:
        fig_clock, ax_clock = plt.subplots(figsize=(7, 5), subplot_kw={"projection": "polar"})
        ax_clock.set_theta_zero_location("N")
        ax_clock.set_theta_direction(-1)
        ax_clock.set_ylim(0, 1.18)
        ax_clock.set_yticks([0.25, 0.5, 0.75, 1.0])
        ax_clock.set_yticklabels([])
        theta_ring = np.linspace(0, 2*np.pi, 361)
        ax_clock.plot(theta_ring, np.full_like(theta_ring, 1.0), alpha=0.18, linewidth=8)
        for k, label in [(0, "0"), (1/3, "3"), (2/3, "6")]:
            theta_k = 2*np.pi*k
            ax_clock.plot([theta_k, theta_k], [0.82, 1.03], linewidth=2)
            ax_clock.text(theta_k, 1.12, label, ha="center", va="center", fontsize=11)
        ax_clock.plot([angulo_relogio, angulo_relogio], [0, 0.84], linewidth=3)
        ax_clock.scatter([angulo_relogio], [0.84], s=100, c=[fase_giro_obs], cmap=obs_paleta, vmin=0, vmax=1, zorder=4)
        ax_clock.text(0, 0.35, "FLUXO", ha="center", va="center", fontsize=13, fontweight="bold")
        ax_clock.set_title("Fase de giro · dial 3–6–9", pad=18)
        fig_clock.tight_layout()
        st.pyplot(fig_clock, use_container_width=True)
        plt.close(fig_clock)
    st.info("Este relógio combina a hora civil com uma fase calculada pelo modelo de pulsos configurado no código. Não é um relógio atômico nem uma medição quântica.")

with obs_tabs[1]:
    st.markdown("**A forma de onda responde à frequência, fase e amplitude selecionadas acima.**")
    n_amostras = 1800
    tempo_eixo = np.linspace(0, obs_duracao, n_amostras)
    sinal = obs_amplitude * np.sin(2*np.pi*obs_frequencia*tempo_eixo + fase_rad_obs)
    # Exibir no máximo alguns ciclos para a forma de onda continuar legível em frequências altas.
    ciclos_visiveis = min(max(3, int(round(ciclos_obs))), 12)
    tempo_visivel = np.linspace(0, ciclos_visiveis / obs_frequencia, 1800)
    sinal_visivel = obs_amplitude * np.sin(2*np.pi*obs_frequencia*tempo_visivel + fase_rad_obs)
    fig_wave, ax_wave = plt.subplots(figsize=(11, 4.2))
    ax_wave.plot(tempo_visivel, sinal_visivel, linewidth=1.7)
    ax_wave.fill_between(tempo_visivel, sinal_visivel, 0, alpha=0.13)
    ax_wave.set_title(f"Forma de onda · {obs_frequencia:g} Hz · fase {obs_fase}°")
    ax_wave.set_xlabel("Tempo (s)")
    ax_wave.set_ylabel("Amplitude normalizada")
    ax_wave.grid(True, alpha=0.22)
    fig_wave.tight_layout()
    st.pyplot(fig_wave, use_container_width=True)
    plt.close(fig_wave)

    # Espectro ilustrativo: pico em f e harmônicos com amplitudes decrescentes.
    harm = np.arange(1, 11)
    harm_freq = obs_frequencia * harm
    harm_amp = obs_amplitude / harm
    fig_spec, ax_spec = plt.subplots(figsize=(11, 3.5))
    markerline, stemlines, baseline = ax_spec.stem(harm_freq, harm_amp)
    ax_spec.set_title("Espectro harmônico ilustrativo")
    ax_spec.set_xlabel("Frequência (Hz)")
    ax_spec.set_ylabel("Amplitude relativa")
    ax_spec.grid(True, alpha=0.2)
    fig_spec.tight_layout()
    st.pyplot(fig_spec, use_container_width=True)
    plt.close(fig_spec)
    st.caption("O espectro é um modelo demonstrativo de harmônicos 1/n, não uma análise FFT de áudio ou de um sinal medido.")

with obs_tabs[2]:
    st.markdown("**Propagação de uma frente de onda**")
    prop_t = np.linspace(0, obs_duracao, 180)
    prop_x = obs_velocidade * prop_t
    prop_phase = 2*np.pi*obs_frequencia*prop_t + fase_rad_obs
    prop_y = obs_amplitude * np.sin(prop_phase)
    pc1, pc2, pc3 = st.columns(3)
    with pc1:
        st.metric("Distância ao final", f"{prop_x[-1]:.6g} m")
    with pc2:
        st.metric("Fase acumulada", f"{np.rad2deg(prop_phase[-1] - fase_rad_obs):,.3g}°".replace(",", "X").replace(".", ",").replace("X", "."))
    with pc3:
        st.metric("Energia cinética de referência", f"{energia_classica_obs:.4e} J")
    fig_prop, ax_prop = plt.subplots(figsize=(11, 4.2))
    sc = ax_prop.scatter(prop_x, prop_y, c=prop_t, cmap=obs_paleta, s=13)
    ax_prop.plot(prop_x, prop_y, alpha=0.25, linewidth=0.8)
    fig_prop.colorbar(sc, ax=ax_prop, label="Tempo (s)")
    ax_prop.set_title("Propagação espacial da onda · cor = tempo")
    ax_prop.set_xlabel("Distância percorrida (m)")
    ax_prop.set_ylabel("Amplitude normalizada")
    ax_prop.grid(True, alpha=0.2)
    fig_prop.tight_layout()
    st.pyplot(fig_prop, use_container_width=True)
    plt.close(fig_prop)

    fig_space, ax_space = plt.subplots(figsize=(11, 2.6))
    ax_space.scatter(prop_x, np.zeros_like(prop_x), c=prop_t, cmap=obs_paleta, s=12)
    ax_space.set_xlim(0, max(float(prop_x[-1]), 1e-9))
    ax_space.set_yticks([])
    ax_space.set_xlabel("Distância (m)")
    ax_space.set_title("Frente de propagação · gradiente cromático = tempo decorrido")
    fig_space.tight_layout()
    st.pyplot(fig_space, use_container_width=True)
    plt.close(fig_space)
    # Diagrama 3D espaço-tempo: coordenadas x, t e amplitude; cor representa a fase.
    t3 = np.linspace(0, obs_duracao, 260)
    x3 = obs_velocidade * t3
    z3 = obs_amplitude * np.sin(2*np.pi*obs_frequencia*t3 + fase_rad_obs)
    fig_3d = plt.figure(figsize=(10, 5.2))
    ax_3d = fig_3d.add_subplot(111, projection="3d")
    pontos_3d = ax_3d.scatter(x3, t3, z3, c=(np.sin(2*np.pi*obs_frequencia*t3 + fase_rad_obs)),
                              cmap=obs_paleta, s=9, alpha=0.88)
    ax_3d.plot(x3, t3, z3, alpha=0.28, linewidth=0.8)
    ax_3d.set_xlabel("Espaço x (m)")
    ax_3d.set_ylabel("Tempo t (s)")
    ax_3d.set_zlabel("Amplitude")
    ax_3d.set_title("Propagação em espaço-tempo · cor = fase")
    fig_3d.colorbar(pontos_3d, ax=ax_3d, pad=0.1, shrink=0.72, label="Fase senoidal")
    fig_3d.tight_layout()
    st.pyplot(fig_3d, use_container_width=True)
    plt.close(fig_3d)
    st.caption("A velocidade é escolhida pelo usuário. A visualização usa x = v·t e uma onda senoidal; não simula por si só relatividade, gravidade ou propagação quântica.")

with obs_tabs[3]:
    st.markdown("**Estrutura galáctica sintética com parâmetros ajustáveis**")
    ga, gb, gc = st.columns(3)
    with ga:
        obs_bracos = st.slider("Braços da galáxia", 2, 8, 4, key="obs_gal_bracos")
        obs_estrelas = st.slider("Partículas estelares", 300, 3000, 1400, step=100, key="obs_gal_estrelas")
    with gb:
        obs_rotacao = st.slider("Torção", 0.2, 2.5, 1.0, step=0.1, key="obs_gal_rotacao")
        obs_dispersao = st.slider("Dispersão", 0.05, 0.8, 0.32, step=0.01, key="obs_gal_disp")
    with gc:
        obs_inclinacao = st.slider("Inclinação", 5, 85, 24, key="obs_gal_inclinacao")
        obs_zoom = st.slider("Escala visual", 0.6, 1.8, 1.0, step=0.1, key="obs_gal_zoom")
    fig_gal = plotar_galaxia_fluxo(obs_bracos, obs_estrelas, obs_rotacao, obs_dispersao, obs_inclinacao)
    # Ajusta a escala de visualização sem alterar o modelo gerador.
    for eixo in fig_gal.axes:
        eixo.set_xlim(-5.2/obs_zoom, 5.2/obs_zoom)
        eixo.set_ylim(-5.2/obs_zoom, 5.2/obs_zoom)
    st.pyplot(fig_gal, use_container_width=True)
    plt.close(fig_gal)
    st.caption("A galáxia é uma composição artística procedural e determinística. Os controles alteram o modelo visual, não dados astronômicos observados.")

with obs_tabs[4]:
    st.markdown("**Mapa de cor de frequência × massa × tempo**")
    # Normalização logarítmica segura para visualizar grandezas de escalas muito diferentes.
    f_grid = np.logspace(np.log10(max(obs_frequencia/100, 1e-9)), np.log10(max(obs_frequencia*10, 1e-8)), 90)
    t_grid = np.linspace(0, obs_duracao, 100)
    FF, TT = np.meshgrid(f_grid, t_grid)
    campo = np.sin(2*np.pi*FF*TT + fase_rad_obs)
    fig_heat, ax_heat = plt.subplots(figsize=(11, 4.5))
    im = ax_heat.pcolormesh(f_grid, t_grid, campo, shading="auto", cmap=obs_paleta, vmin=-1, vmax=1)
    ax_heat.set_xscale("log")
    ax_heat.set_xlabel("Frequência (Hz) · escala logarítmica")
    ax_heat.set_ylabel("Tempo (s)")
    ax_heat.set_title("Mapa de fase · cor representa amplitude senoidal")
    fig_heat.colorbar(im, ax=ax_heat, label="Amplitude normalizada")
    fig_heat.tight_layout()
    st.pyplot(fig_heat, use_container_width=True)
    plt.close(fig_heat)

    # Massa e frequência em escala logarítmica para mostrar a diferença de ordens de grandeza.
    m_plot = np.logspace(-12, 12, 160)
    f_plot = np.full_like(m_plot, obs_frequencia)
    raio_plot = np.clip(30 + 6*np.log10(m_plot + 1e-300) + 72, 3, 180)
    fig_mass, ax_mass = plt.subplots(figsize=(11, 3.5))
    pts = ax_mass.scatter(m_plot, f_plot, c=np.log10(m_plot), s=raio_plot, cmap=obs_paleta, alpha=0.7)
    ax_mass.set_xscale("log")
    ax_mass.set_xlabel("Massa de referência (kg) · faixa ilustrativa")
    ax_mass.set_ylabel("Frequência escolhida (Hz)")
    ax_mass.set_title("Mapa de escala de massa · tamanho/cor codificam a ordem de grandeza")
    fig_mass.colorbar(pts, ax=ax_mass, label="log₁₀(massa em kg)")
    fig_mass.grid(True, alpha=0.2)
    fig_mass.tight_layout()
    st.pyplot(fig_mass, use_container_width=True)
    plt.close(fig_mass)
    st.caption("As cores são codificações visuais de grandezas normalizadas. Não significam que frequência determine massa; o gráfico de massa é uma escala ilustrativa.")

with obs_tabs[5]:
    st.markdown("**Campo gravitacional clássico de uma massa pontual**")
    st.caption("Modelo newtoniano idealizado, útil para visualizar como a intensidade diminui com o quadrado da distância. Não é uma simulação de gravidade quântica.")
    dist_min, dist_max = st.slider("Faixa de distância ao centro da massa (m)", 0.1, 10000.0, (0.5, 100.0), key="obs_grav_range")
    distancias = np.geomspace(dist_min, dist_max, 240)
    aceleracoes = G_NEWTON * obs_massa / np.square(distancias)
    forca_ref = G_NEWTON * obs_massa / (dist_min**2)
    ga1, ga2, ga3 = st.columns(3)
    with ga1:
        st.metric("Massa de referência", f"{obs_massa:.4e} kg")
    with ga2:
        st.metric("Aceleração em r mínimo", f"{forca_ref:.4e} m/s²")
    with ga3:
        st.metric("Aceleração em r máximo", f"{G_NEWTON*obs_massa/(dist_max**2):.4e} m/s²")
    fig_grav, ax_grav = plt.subplots(figsize=(10, 4.2))
    ax_grav.loglog(distancias, aceleracoes, linewidth=2.2)
    ax_grav.fill_between(distancias, aceleracoes, alpha=0.15)
    ax_grav.set_xlabel("Distância ao centro r (m) · escala log")
    ax_grav.set_ylabel("Aceleração g = GM/r² (m/s²) · escala log")
    ax_grav.set_title("Campo gravitacional newtoniano idealizado")
    ax_grav.grid(True, which="both", alpha=0.2)
    fig_grav.tight_layout()
    st.pyplot(fig_grav, use_container_width=True)
    plt.close(fig_grav)
    st.write("Equação: **g(r) = G · M / r²**. O resultado depende da massa e da distância definidas. O modelo considera uma massa pontual isolada.")

with obs_tabs[6]:
    st.markdown("**Equações utilizadas neste painel**")
    eq_df = pd.DataFrame([
        {"Grandeza": "Período", "Equação": "T = 1/f", "Resultado": f"{periodo_obs:.8g} s", "Natureza": "Relação matemática/física"},
        {"Grandeza": "Comprimento de onda", "Equação": "λ = v/f", "Resultado": f"{comprimento_onda_obs:.8g} m", "Natureza": "Modelo de onda com velocidade selecionada"},
        {"Grandeza": "Energia do fóton", "Equação": "E = h·f", "Resultado": f"{energia_quantum_obs:.8e} J", "Natureza": "Relação física para fótons"},
        {"Grandeza": "Energia cinética clássica", "Equação": "Ec = ½mv²", "Resultado": f"{energia_classica_obs:.8e} J", "Natureza": "Modelo clássico; requer massa e velocidade coerentes"},
        {"Grandeza": "Distância propagada", "Equação": "x = v·t", "Resultado": f"{obs_velocidade*obs_duracao:.8g} m", "Natureza": "Movimento uniforme idealizado"},
        {"Grandeza": "Fase", "Equação": "θ = 2πft + φ", "Resultado": f"{(2*np.pi*obs_frequencia*obs_duracao + fase_rad_obs):.8g} rad", "Natureza": "Modelo senoidal"},
    ])
    st.dataframe(eq_df, use_container_width=True, hide_index=True)
    st.markdown("#### Leitura responsável")
    st.write("- Os resultados numéricos são recalculados a partir dos controles e das equações exibidas.")
    st.write("- Constantes autorais do Fluxo Matemático podem ser exploradas como parâmetros do modelo, mas não devem ser apresentadas como constantes físicas universais sem validação independente.")
    st.write("- A massa de referência não entra na equação de energia do fóton; ela é usada apenas na energia cinética clássica mostrada separadamente.")
    st.download_button("⬇️ Exportar resultados do observatório (CSV)", data=eq_df.to_csv(index=False).encode("utf-8-sig"),
                       file_name="observatorio_fluxo_resultados.csv", mime="text/csv", key="obs_export_csv")

# =============================================================================
# FIM DO CÓDIGO
# =============================================================================