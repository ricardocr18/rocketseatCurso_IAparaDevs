# 🎨 Questão 1: Como o Ray Tracing Calcula a Cor de um Pixel

## 📋 Prompt Utilizado

### **Entrada:**
```
Como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada
```

### **Técnica Aplicada:**
**Zero-Shot** - Pergunta direta sem exemplos prévios, confiando no conhecimento prévio do modelo sobre Ray Tracing.

### **Justificativa:**
Optou-se pela utilização da técnica de Zero-Shot, considerando que o Ray Tracing é uma tecnologia amplamente documentada e consolidada, com princípios e aplicações bem estabelecidos. Além disso, a questão apresentada é bastante objetiva, não exigindo exemplos ou contexto adicional para que o modelo compreenda e elabore uma resposta precisa. Essa abordagem foi escolhida por sua eficiência, dispensando a necessidade de fornecer exemplos específicos e confiando na capacidade do modelo de interpretar diretamente a solicitação com base em seu treinamento prévio.

---

## 🤖 Resposta Obtida da IA Generativa

### **Como o Ray Tracing Calcula a Cor de um Pixel**

O algoritmo de **Ray Tracing** (rastreamento de raios) calcula a cor de um pixel simulando o comportamento físico da luz na cena virtual. O processo segue estas etapas principais:

---

## 🔬 **Processo Detalhado:**

### **1. Lançamento do Raio Primário**
- Para cada pixel da tela, um **raio primário** é lançado da câmera (olho do observador) através do pixel
- O raio é representado por:
  - **Origem:** Posição da câmera
  - **Direção:** Vetor que aponta do centro da câmera através do centro do pixel

**Fórmula matemática:**
```
Raio(t) = Origem + t × Direção
onde t ≥ 0
```

---

### **2. Teste de Interseção**
O raio viaja pela cena até encontrar o primeiro objeto. O algoritmo calcula:
- **Ponto de interseção** (hit point)
- **Normal da superfície** nesse ponto
- **Material do objeto** (propriedades de reflexão, refração, cor base)

**Teste de interseção comum:**
- Esferas: Resolução de equação quadrática
- Triângulos: Algoritmo de Möller-Trumbore
- Planos: Produto escalar

---

### **3. Cálculo da Iluminação Local**

No ponto de interseção, o algoritmo calcula a **contribuição de luz direta** de cada fonte de luz:

#### **Modelo de Iluminação (Phong/Blinn-Phong):**

```
Cor_Final = Ambiente + Difusa + Especular
```

**a) Componente Ambiente (Ambient):**
```
I_ambiente = K_a × I_luz_ambiente
```
- Iluminação uniforme independente da posição

**b) Componente Difusa (Diffuse - Lambert):**
```
I_difusa = K_d × I_luz × max(0, N · L)
```
Onde:
- `N` = Normal da superfície
- `L` = Vetor direção da luz
- `K_d` = Coeficiente de reflexão difusa (cor do material)

**c) Componente Especular (Specular):**
```
I_especular = K_s × I_luz × max(0, R · V)^n
```
Onde:
- `R` = Vetor de reflexão da luz
- `V` = Vetor de visão (direção da câmera)
- `n` = Brilho (shininess)

---

### **4. Raios de Sombra (Shadow Rays)**

Para cada fonte de luz, lança-se um **raio de sombra** do ponto de interseção até a luz:
- Se o raio atinge um objeto antes de alcançar a luz → **pixel em sombra** (não adiciona contribuição dessa luz)
- Se o raio chega à luz sem obstrução → **pixel iluminado** (adiciona contribuição)

---

### **5. Reflexão e Refração (Raios Secundários)**

#### **Reflexão (Recursive Ray Tracing):**
Se o material é refletivo:
1. Calcula direção do raio refletido:
   ```
   R = D - 2(D · N)N
   ```
2. Lança novo raio na direção refletida
3. Adiciona cor refletida multiplicada pelo coeficiente de reflexão

#### **Refração (Transmitted Rays):**
Se o material é transparente:
1. Aplica Lei de Snell:
   ```
   n₁ × sen(θ₁) = n₂ × sen(θ₂)
   ```
2. Calcula direção do raio refratado
3. Adiciona cor transmitida

**Limite de recursão:** 3-5 níveis para evitar cálculos infinitos

---

### **6. Combinação das Cores**

A cor final do pixel é a **soma ponderada** de todas as contribuições:

```
Cor_Pixel = Cor_Local + 
            K_reflexão × Cor_Refletida + 
            K_refração × Cor_Refratada
```

---

## 🎨 **Exemplo Prático:**

### **Cenário: Esfera vermelha iluminada**

```
1. Raio primário atinge esfera no ponto P
2. Normal N calculada em P
3. Iluminação local:
   - Ambiente: RGB(0.1, 0, 0) [vermelho escuro]
   - Difusa: RGB(0.8, 0, 0) × cos(ângulo luz)
   - Especular: RGB(1, 1, 1) × brilho^30
4. Raio de sombra verifica obstruções
5. Se esfera tem reflexão (ex: 30%):
   - Lança raio refletido
   - Adiciona 30% da cor do que for refletido
6. Cor final = soma de todas contribuições
```

---

## 📊 **Pseudocódigo Simplificado:**

```python
def trace_ray(ray, depth):
    if depth > MAX_DEPTH:
        return COR_FUNDO
    
    # 1. Encontrar interseção mais próxima
    hit = find_closest_intersection(ray, scene)
    
    if not hit:
        return COR_FUNDO
    
    # 2. Iluminação local (Phong)
    cor_local = calcular_phong(hit.point, hit.normal, hit.material)
    
    # 3. Verificar sombras
    for luz in luzes:
        shadow_ray = Ray(hit.point, luz.position - hit.point)
        if tem_obstrucao(shadow_ray):
            cor_local *= 0.2  # Sombreamento
    
    # 4. Reflexão recursiva
    cor_refletida = RGB(0, 0, 0)
    if hit.material.reflectivity > 0:
        reflected_ray = reflect(ray, hit.normal)
        cor_refletida = trace_ray(reflected_ray, depth + 1)
    
    # 5. Refração recursiva
    cor_refratada = RGB(0, 0, 0)
    if hit.material.transparency > 0:
        refracted_ray = refract(ray, hit.normal, hit.material.ior)
        cor_refratada = trace_ray(refracted_ray, depth + 1)
    
    # 6. Combinar cores
    cor_final = (cor_local + 
                 hit.material.reflectivity * cor_refletida +
                 hit.material.transparency * cor_refratada)
    
    return clamp(cor_final, 0, 1)


# Para cada pixel (x, y):
def render_pixel(x, y):
    ray = gerar_raio_primario(camera, x, y)
    cor = trace_ray(ray, depth=0)
    set_pixel(x, y, cor)
```

---

## 🔑 **Conceitos-Chave:**

| Conceito | Descrição |
|----------|-----------|
| **Raio Primário** | Raio lançado da câmera através do pixel |
| **Interseção** | Ponto onde o raio atinge um objeto |
| **Normal** | Vetor perpendicular à superfície no ponto de interseção |
| **Iluminação de Phong** | Modelo que combina luz ambiente, difusa e especular |
| **Raio de Sombra** | Raio do ponto de interseção até a luz (detecta sombras) |
| **Reflexão** | Raio secundário que simula espelhos |
| **Refração** | Raio secundário que simula transparência (Lei de Snell) |
| **Recursão** | Raios secundários podem gerar mais raios (profundidade limitada) |

---

## 🎯 **Vantagens do Ray Tracing:**

✅ **Realismo físico:** Simula comportamento real da luz  
✅ **Reflexões perfeitas:** Espelhos e superfícies metálicas  
✅ **Refrações precisas:** Vidro, água, cristais  
✅ **Sombras suaves:** Penumbra e sombras complexas  
✅ **Iluminação global:** Luz indireta (com extensões como Path Tracing)  

---

## ⚡ **Desvantagens:**

❌ **Alto custo computacional:** Milhões de raios por frame  
❌ **Lento para tempo real:** Tradicionalmente usado em renderização offline  
❌ **Ruído:** Requer muitas amostras para imagens limpas  

**Solução moderna:** GPUs com **Ray Tracing em hardware** (NVIDIA RTX, AMD RDNA 2)

---

## 📚 **Referências:**

- **Whitted, Turner** (1980). "An Improved Illumination Model for Shaded Display"
- **Kajiya, James** (1986). "The Rendering Equation"
- **NVIDIA RTX Technology:** https://www.nvidia.com/en-us/geforce/technologies/ray-tracing/
- **Peter Shirley's Ray Tracing in One Weekend:** https://raytracing.github.io/

---

**Data da Consulta:** 02/01/2025  
**Ferramenta IA:** ChatGPT / Claude / Gemini  
**Técnica:** Zero-Shot Prompting